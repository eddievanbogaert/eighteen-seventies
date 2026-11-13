#!/usr/bin/env python3
"""Produce a clean reading copy of a chapter, with the claim markers removed.

    python3 tools/reading_copy.py chapters/12-bell-telephone-patent.md
    python3 tools/reading_copy.py --all --out build/

The manuscript in /chapters carries a claim id after every specific assertion,
so that any sentence can be traced to the CLAIMS.md row that licenses it. That
apparatus is load-bearing and stays in the repository. It also makes the prose
unreadable as prose, which matters, because a draft nobody can read as a reader
does not get judged as writing.

This script exists so the two needs do not have to fight. The repository keeps
the markers; this prints the version a reader sees.

It is deliberately one-way. There is no script that puts markers back, because
a sentence that lost its marker has lost its licence and should be caught by
tools/check.py rather than repaired automatically.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

CLAIM_REF = re.compile(r"\s*\[C\d{2}-\d{3}\]")
# Stub scaffolding a reader should never meet.
STUB_BLOCK = re.compile(
    r"^> \*\*Stub — no narrative content\.\*\*.*?(?=\n\n)", re.S | re.M
)
DROP_SECTIONS = ("## Drafting blockers",)


def strip(text: str, keep_apparatus: bool = False) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    text = CLAIM_REF.sub("", text)
    if not keep_apparatus:
        text = STUB_BLOCK.sub("", text)
        for heading in DROP_SECTIONS:
            text = re.sub(
                rf"^{re.escape(heading)}\n.*?(?=^## |\Z)", "", text, flags=re.S | re.M
            )
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def words(text: str) -> int:
    return len(re.findall(r"\b[\w'’-]+\b", text))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", help="chapter files")
    ap.add_argument("--all", action="store_true", help="every chapter")
    ap.add_argument("--out", help="write .md files into this directory")
    ap.add_argument("--keep-apparatus", action="store_true",
                    help="keep drafting blockers and stub notices")
    args = ap.parse_args()

    paths = sorted((ROOT / "chapters").glob("*.md")) if args.all else [
        pathlib.Path(p) for p in args.paths
    ]
    if not paths:
        ap.error("give chapter paths or --all")

    out = pathlib.Path(args.out) if args.out else None
    if out:
        out.mkdir(parents=True, exist_ok=True)

    total = 0
    for p in paths:
        if not p.exists():
            print(f"missing: {p}", file=sys.stderr)
            return 1
        text = strip(p.read_text(encoding="utf-8"), args.keep_apparatus)
        total += words(text)
        if out:
            (out / p.name).write_text(text, encoding="utf-8")
            print(f"{p.name}: {words(text):,} words")
        else:
            print(text)
    if out:
        print(f"\n{len(paths)} chapter(s), {total:,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
