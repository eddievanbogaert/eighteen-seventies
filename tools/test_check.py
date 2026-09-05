#!/usr/bin/env python3
"""Tests for tools/check.py.

    python3 tools/test_check.py

A check that passes because it never looks at anything is worse than no check,
because it produces confidence. Each case below copies the repository to a
temporary directory, breaks exactly one thing, and asserts that `check.py`
notices and says something useful about it. The last case asserts that the
unmodified repository passes, so the suite fails if the checker starts
rejecting everything.

Standard library only, and no test framework, for the same reason `check.py`
has no dependencies: a test that needs installing is a test that gets skipped.
"""

from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (name, path relative to repo, find, replace, expected fragment of the error)
CASES = [
    (
        "unquoted date flag",
        "chapters/07-coinage-act-of-1873.md",
        'date_range_verified: "n"',
        "date_range_verified: n",
        "must be \"y\" or \"n\" with quotes",
    ),
    (
        "unknown thread",
        "chapters/07-coinage-act-of-1873.md",
        "threads: [money]",
        "threads: [finance]",
        "unknown thread(s) finance",
    ),
    (
        "empty threads without a recorded decision",
        "chapters/07-coinage-act-of-1873.md",
        "threads: [money]",
        "threads: []",
        "must be a recorded decision",
    ),
    (
        "status off the ladder",
        "chapters/07-coinage-act-of-1873.md",
        "status: stub",
        "status: nearly-done",
        "is not one of",
    ),
    (
        "claim cites a source not in the manifest",
        "research/CLAIMS.md",
        "friedman-schwartz-monetary-history",
        "friedman-schwartz-monetry-history",
        "is not in sources/MANIFEST.md",
    ),
    (
        "chapter cites a source with no verified row",
        "chapters/07-coinage-act-of-1873.md",
        "sources: []",
        "sources: [unger-greenback-era]",
        "no verified CLAIMS.md row",
    ),
    (
        "chapter cites a source that does not exist",
        "chapters/07-coinage-act-of-1873.md",
        "sources: []",
        "sources: [nonesuch-1873]",
        "not in the manifest",
    ),
    (
        "open_questions out of step with QUESTIONS.md",
        "chapters/07-coinage-act-of-1873.md",
        "open_questions: [Q07-1, Q07-2, Q07-3, Q07-4, Q07-5]",
        "open_questions: [Q07-1, Q07-2, Q07-3, Q07-4]",
        "missing Q07-5",
    ),
    (
        "question dropped from the triage table",
        "notes/question-triage.md",
        "| 12 | Q12-1, Q12-2, Q12-3, Q12-4 | Q12-5 | | | |",
        "| 12 | Q12-1, Q12-2, Q12-3 | Q12-5 | | | |",
        "not in the triage table",
    ),
    (
        "stated distribution no longer matches the table",
        "notes/question-triage.md",
        "**Distribution: 85 gate, 26 parallel, 5 authorial, 6 convention.**",
        "**Distribution: 84 gate, 26 parallel, 5 authorial, 6 convention.**",
        "stated gate count is 84",
    ),
    (
        "stated question total drifts",
        "notes/question-triage.md",
        "All 122 questions in",
        "All 121 questions in",
        "but QUESTIONS.md has 122",
    ),
    (
        "thesis-critical count drifts",
        "notes/README.md",
        "the seven that are thesis-critical",
        "the nine that are thesis-critical",
        "but the triage table marks 7",
    ),
    (
        "chapter-order date disagrees with the chapter file",
        "notes/chapter-order.md",
        "| 07 | Coinage Act of 1873 | 1873 | money |",
        "| 07 | Coinage Act of 1873 | 1873-02 | money |",
        "disagrees with the chapter file's",
    ),
    (
        "chapter-order home thread disagrees with the chapter file",
        "notes/chapter-order.md",
        "| 16 | Satsuma Rebellion | 1877 | empire |",
        "| 16 | Satsuma Rebellion | 1877 | machines |",
        "home thread 'machines' disagrees",
    ),
    (
        "unverified year asserted in chapter prose",
        "chapters/12-bell-telephone-patent.md",
        "  Filing, granting, and first successful transmission are three dates.",
        "  The patent was granted in March 1876.",
        "year 1876 in prose",
    ),
    (
        "page number in a chapter",
        "chapters/12-bell-telephone-patent.md",
        "- Open questions: `/research/QUESTIONS.md` → Q12.",
        "- See bruce-bell, pp. 142-148.",
        "a page number",
    ),
    (
        "manifest row marked read but not acquired",
        "sources/MANIFEST.md",
        '| 1963 | monograph | "n" | "n" |',
        '| 1963 | monograph | "n" | "y" |',
        "marked read but not acquired",
    ),
    (
        "unquoted manifest flags",
        "sources/MANIFEST.md",
        '| 1963 | monograph | "n" | "n" |',
        "| 1963 | monograph | n | n |",
        "AGENTS.md requires the quoted form here too",
    ),
    (
        "duplicate source key",
        "sources/MANIFEST.md",
        "| foner-reconstruction | Eric Foner |",
        "| wicker-banking-panics | Eric Foner |",
        "duplicate source key",
    ),
    (
        "unknown source type",
        "sources/MANIFEST.md",
        "| 1963 | monograph |",
        "| 1963 | book |",
        "type 'book' is not one of",
    ),
    (
        "source dropped from the acquisition worksheet",
        "sources/ACQUISITION.md",
        "`wicker-banking-panics`",
        "",
        "has no route in the worksheet",
    ),
    (
        "mistyped source key in the acquisition worksheet",
        "sources/ACQUISITION.md",
        "`wicker-banking-panics`",
        "`wicker-banking-panic`",
        "looks like a source key but is not in the manifest",
    ),
    (
        "source given two routes",
        "sources/ACQUISITION.md",
        "`white-railroaded`, `wicker-banking-panics`",
        "`white-railroaded`, `white-railroaded`, `wicker-banking-panics`",
        "each source takes exactly one route",
    ),
    (
        "dangling question reference in a chapter",
        "chapters/07-coinage-act-of-1873.md",
        "- Open questions: `/research/QUESTIONS.md` → Q07.",
        "- See Q07-9.",
        "references Q07-9, which is not in QUESTIONS.md",
    ),
    (
        "dangling question reference in a note",
        "notes/voice-and-shape.md",
        "Q03-3 and\nQ03-4",
        "Q03-3 and\nQ03-9",
        "references Q03-9, which is not in QUESTIONS.md",
    ),
    (
        "manifest relevance cites a chapter that does not exist",
        "sources/MANIFEST.md",
        "money; ch 07, 10, 21 — its series begin at 1867",
        "money; ch 07, 10, 22 — its series begin at 1867",
        "relevance cites chapter 22, which does not exist",
    ),
    (
        "note missing from the /notes index",
        "notes/README.md",
        "- `voice-and-shape.md`",
        "- `voice-and-shape-renamed.md`",
        "does not list voice-and-shape.md",
    ),
    (
        "duplicate question id",
        "research/QUESTIONS.md",
        "- **Q12-5** How fast did installation",
        "- **Q12-4** How fast did installation",
        "duplicate question id",
    ),
]


def run(repo: pathlib.Path) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, str(repo / "tools" / "check.py")],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout + result.stderr


def main() -> int:
    failures = []

    with tempfile.TemporaryDirectory() as tmp:
        clean = pathlib.Path(tmp) / "clean"
        shutil.copytree(
            ROOT, clean, ignore=shutil.ignore_patterns(".git", "__pycache__")
        )
        code, output = run(clean)
        if code != 0:
            failures.append(
                "the unmodified repository does not pass:\n" + output
            )
        else:
            print("ok    unmodified repository passes")

    for name, rel, find, replace, expected in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            repo = pathlib.Path(tmp) / "repo"
            shutil.copytree(
                ROOT, repo, ignore=shutil.ignore_patterns(".git", "__pycache__")
            )
            target = repo / rel
            text = target.read_text(encoding="utf-8")
            if find not in text:
                failures.append(f"{name}: fixture text not found in {rel}: {find!r}")
                print(f"SKIP  {name} (fixture out of date)")
                continue
            target.write_text(text.replace(find, replace, 1), encoding="utf-8")

            code, output = run(repo)
            if code == 0:
                failures.append(f"{name}: check.py passed a repository it should reject")
                print(f"FAIL  {name} — not detected")
            elif expected not in output:
                failures.append(
                    f"{name}: detected, but no message contained {expected!r}\n{output}"
                )
                print(f"FAIL  {name} — wrong message")
            else:
                print(f"ok    {name}")

    # A transcription with no provenance is a new file rather than an edit.
    with tempfile.TemporaryDirectory() as tmp:
        repo = pathlib.Path(tmp) / "repo"
        shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        (repo / "primary" / "coinage-act-1873.md").write_text(
            "# Coinage Act of 1873\n\nSome transcribed text.\n", encoding="utf-8"
        )
        code, output = run(repo)
        if code == 0 or "provenance" not in output:
            failures.append("transcription without provenance was not rejected")
            print("FAIL  transcription without provenance")
        else:
            print("ok    transcription without provenance")

    print()
    if failures:
        print(f"{len(failures)} failure(s):")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print(f"all {len(CASES) + 2} cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
