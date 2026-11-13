#!/usr/bin/env python3
"""Check the drafts in notes/drafts/ against CLAIMS.md.

    python3 tools/check_drafts.py

tools/check.py audits /chapters, which is where finished prose goes. Drafts
live in notes/drafts/ until their claims carry the author's "y" (see
EXCEPTIONS.md E-1), so they are outside that audit — and were therefore
unchecked, which is the wrong way round: a draft is where mistakes are made.

Three things are checked, all of them rules CLAIMS.md already states:

* every claim marker resolves to a row;
* a marker in a draft for chapter N points at a row for chapter N, because
  "a claim used in two chapters gets two rows, since each use can drift";
* the draft does not silently cite a row marked verified "n" without the
  draft saying somewhere that it is unverified.

Exits non-zero on any failure.
"""
from __future__ import annotations
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = re.compile(r"\[(C\d{2}-\d{3})\]")


def claims() -> dict[str, tuple[str, str]]:
    out = {}
    for line in (ROOT / "research" / "CLAIMS.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("| C") and line.count("|") >= 6:
            c = [x.strip() for x in line.strip("|").split("|")]
            out[c[0]] = (c[2].zfill(2), c[4].strip('"'))
    return out


def main() -> int:
    rows = claims()
    drafts = sorted((ROOT / "notes" / "drafts").glob("*.md"))
    if not drafts:
        print("no drafts"); return 0
    errors = 0
    for f in drafts:
        text = f.read_text(encoding="utf-8")
        chapter = f.name[:2]
        refs = sorted(set(REF.findall(text)))
        says_unverified = "verified" in text.lower() and '"n"' in text
        for r in refs:
            if r not in rows:
                print(f"  {f.name}: cites {r}, which has no row"); errors += 1
                continue
            row_ch, flag = rows[r]
            if row_ch != chapter:
                print(f"  {f.name}: cites {r}, whose row is chapter {row_ch} — "
                      "a claim used in two chapters needs a row in each"); errors += 1
            if flag == "n" and not says_unverified:
                print(f"  {f.name}: cites unverified {r} without saying the draft "
                      "rests on unverified claims"); errors += 1
        print(f"  {f.name}: {len(refs)} refs"
              f"{'' if errors == 0 else ''}")
    print("ok" if not errors else f"{errors} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
