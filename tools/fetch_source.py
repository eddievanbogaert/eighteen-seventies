#!/usr/bin/env python3
"""Retrieve one source document and record its provenance.

    python3 tools/fetch_source.py URL --key SOURCE_KEY --form ocr \
        --holding "Library of Congress, Manuscript Division"

One URL per invocation, deliberately. This is a research tool for reading a
handful of documents carefully, not a crawler, and it should never be wrapped
in a loop over a list of hosts.

What it does beyond fetching:

* **Records a SHA-256 of the exact bytes.** This is the part that matters for
  auditing. A row in RETRIEVED.md that carries a hash lets anyone re-fetch the
  document years later and prove they are reading what the claim was checked
  against — or prove that the page has changed since, which is just as useful.
* **Saves the bytes to a cache outside version control.** The repository keeps
  the hash and the transcription, not a pile of PDFs.
* **Identifies itself honestly.** The user agent says what this is and that it
  is a research retrieval. It does not pretend to be a browser. A site that
  declines to serve this tool has declined, and the answer is to find another
  copy or ask the holding institution, never to disguise the request.
* **Honours robots.txt**, and refuses a path the site disallows.

Rate limiting is one request at a time with a pause, because the collections
this book depends on are public goods maintained on small budgets.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / "sources" / "cache"
RETRIEVED = ROOT / "sources" / "RETRIEVED.md"

UA = (
    "eighteen-seventies-research/1.0 "
    "(single-document retrieval for a history book; not a crawler)"
)
FORMS = ("image", "transcription", "ocr", "born-digital")
PAUSE = 2.0


def robots_allow(url: str) -> tuple[bool, str]:
    parts = urllib.parse.urlsplit(url)
    robots = f"{parts.scheme}://{parts.netloc}/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    try:
        req = urllib.request.Request(robots, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            rp.parse(r.read().decode("utf-8", "replace").splitlines())
    except Exception as exc:  # no robots.txt, or unreachable: proceed politely
        return True, f"robots.txt unavailable ({exc.__class__.__name__}); proceeding"
    return (rp.can_fetch(UA, url), "robots.txt consulted")


def fetch(url: str) -> tuple[bytes, str, int]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read(), r.headers.get("Content-Type", ""), r.status


def extension(content_type: str, url: str) -> str:
    for token, ext in (
        ("pdf", ".pdf"), ("json", ".json"), ("xml", ".xml"),
        ("html", ".html"), ("plain", ".txt"), ("jp2", ".jp2"),
        ("tiff", ".tif"), ("jpeg", ".jpg"), ("png", ".png"),
    ):
        if token in content_type.lower():
            return ext
    return pathlib.Path(urllib.parse.urlsplit(url).path).suffix or ".bin"


def add_row(key, url, today, form, holding, note, digest, path) -> None:
    text = RETRIEVED.read_text(encoding="utf-8")
    text = text.replace("| _(none yet)_ | | | | | |\n", "")
    notes = f"{note} sha256 `{digest[:16]}…` cached at `{path}`."
    row = f"| {key} | {url} | {today} | {form} | {holding} | {notes} |\n"
    if url in text:
        print("note: this URL already has a row; not duplicating it", file=sys.stderr)
        return
    RETRIEVED.write_text(text.rstrip("\n") + "\n" + row, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("url")
    ap.add_argument("--key", required=True, help="source_key from MANIFEST.md")
    ap.add_argument("--form", required=True, choices=FORMS)
    ap.add_argument("--holding", required=True, help="holding institution")
    ap.add_argument("--note", default="", help="what was taken from it")
    ap.add_argument("--no-log", action="store_true", help="fetch without logging")
    args = ap.parse_args()

    allowed, why = robots_allow(args.url)
    print(f"  {why}")
    if not allowed:
        print(f"refused: robots.txt disallows {args.url}", file=sys.stderr)
        print("find another copy, or ask the holding institution.", file=sys.stderr)
        return 2

    time.sleep(PAUSE)
    try:
        body, ctype, status = fetch(args.url)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} from {args.url}", file=sys.stderr)
        if e.code in (403, 429):
            print(
                "the site declined to serve this tool. Do not disguise the "
                "request — find another copy or ask the institution.",
                file=sys.stderr,
            )
        return 1
    except Exception as e:
        print(f"failed: {e}", file=sys.stderr)
        return 1

    digest = hashlib.sha256(body).hexdigest()
    dest = CACHE / args.key
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / f"{digest[:16]}{extension(ctype, args.url)}"
    out.write_bytes(body)
    rel = out.relative_to(ROOT)

    print(f"  HTTP {status}  {len(body):,} bytes  {ctype}")
    print(f"  sha256 {digest}")
    print(f"  saved  {rel}")

    if not args.no_log:
        add_row(
            args.key, args.url, dt.date.today().isoformat(),
            args.form, args.holding, args.note, digest, rel,
        )
        print(f"  logged in {RETRIEVED.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
