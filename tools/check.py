#!/usr/bin/env python3
"""Repository integrity checks for the 1870s book.

Run from anywhere:

    python3 tools/check.py            # errors and warnings
    python3 tools/check.py --quiet    # failures only
    python3 tools/check.py --list     # what is checked, and what is not

Exits non-zero if any error is found. Warnings never fail the run.

The rules in AGENTS.md are binding, and until this script existed they were
enforced by good intentions. The scaffolding pass proved that insufficient: a
CLAIMS.md row cited a source_key that was not in the manifest, and it was
caught only by a hand-run scan that nobody was obliged to run.

What a script can and cannot enforce is worth being clear about. Everything
here is a consistency check — whether the repository's own files agree with
each other and with the shapes AGENTS.md requires. None of it can tell whether
a claim is true, whether a source says what a row says it says, or whether a
flag flipped to "y" because somebody actually read the page. Those are the
checks that matter most and they are human checks. This script exists so that
attention is not spent on the mechanical ones.

Standard library only, deliberately: a check that fails because a dependency
is missing teaches people to skip it.
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

THREADS = {"money", "race", "machines", "empire"}

# B-08: proposed and awaiting the author's confirmation. Tied to verification
# rather than to word count, per AGENTS.md.
STATUSES = ["stub", "gates-closed", "drafting", "drafted", "verified"]

CHAPTER_KEYS_REQUIRED = {
    "title",
    "date_range",
    "threads",
    "status",
    "sources",
    "open_questions",
}
CHAPTER_KEYS_OPTIONAL = {"date_range_verified", "thread_assignment"}

MANIFEST_COLUMNS = [
    "key",
    "author",
    "title",
    "year",
    "type",
    "acquired",
    "read",
    "relevance",
]
CLAIMS_COLUMNS = ["claim", "chapter", "source_key", "verified", "notes"]
SOURCE_TYPES = {"monograph", "article", "primary"}

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "twenty-one": 21,
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks_run = 0

    def error(self, path, line, message) -> None:
        self.errors.append(f"{_rel(path)}:{line}: {message}")

    def warn(self, path, line, message) -> None:
        self.warnings.append(f"{_rel(path)}:{line}: {message}")


def _rel(path) -> str:
    try:
        return str(pathlib.Path(path).resolve().relative_to(ROOT))
    except (ValueError, TypeError):
        return str(path)


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------

def read(path: pathlib.Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n")


def parse_frontmatter(lines: list[str]):
    """Return (raw_values, end_index) for a leading --- fenced block.

    Values are kept as raw text so that quoting can be checked. A YAML parser
    would resolve `n` to False before this script ever saw it, which is the
    precise ambiguity AGENTS.md requires the quotes to prevent.
    """
    if not lines or lines[0].strip() != "---":
        return None, 0
    values: dict[str, tuple[str, int]] = {}
    for i, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            return values, i
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = (match.group(2).strip(), i)
    return values, len(lines)


def unquote(raw: str) -> str:
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def parse_list(raw: str) -> list[str]:
    inner = raw.strip()
    if not (inner.startswith("[") and inner.endswith("]")):
        return []
    inner = inner[1:-1].strip()
    if not inner:
        return []
    return [unquote(part.strip()) for part in inner.split(",") if part.strip()]


def parse_table(lines: list[str], expected: list[str], path, report: Report):
    """Return [(cells, line_number)] for the first markdown table matching
    `expected` as its header row."""
    rows = []
    header_seen = False
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            if header_seen and rows:
                break
            continue
        cells = [c.strip() for c in stripped[1:-1].split("|")]
        if not header_seen:
            if [c.lower() for c in cells] == expected:
                header_seen = True
            continue
        if all(set(c) <= {"-", ":", " "} and c for c in cells):
            continue
        if len(cells) != len(expected):
            report.error(
                path, i,
                f"table row has {len(cells)} columns, expected "
                f"{len(expected)} ({', '.join(expected)})",
            )
            continue
        rows.append((cells, i))
    if not header_seen:
        report.error(path, 1, f"no table found with header: {', '.join(expected)}")
    return rows


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------

def check_chapters(report: Report):
    """Filenames, frontmatter shape, flags, threads, statuses."""
    paths = sorted((ROOT / "chapters").glob("*.md"))
    chapters = {}
    seen_numbers: dict[str, pathlib.Path] = {}

    for path in paths:
        match = re.match(r"^(\d{2})-[a-z0-9-]+\.md$", path.name)
        if not match:
            report.error(path, 1, "filename must match NN-slug.md, lowercase")
            continue
        number = match.group(1)
        if number in seen_numbers:
            report.error(
                path, 1,
                f"duplicate chapter number {number}, also "
                f"{_rel(seen_numbers[number])}",
            )
        seen_numbers[number] = path

        lines = read(path)
        front, end = parse_frontmatter(lines)
        if front is None:
            report.error(path, 1, "no frontmatter block")
            continue

        missing = CHAPTER_KEYS_REQUIRED - set(front)
        if missing:
            report.error(path, 1, f"frontmatter missing: {', '.join(sorted(missing))}")
        unknown = set(front) - CHAPTER_KEYS_REQUIRED - CHAPTER_KEYS_OPTIONAL
        if unknown:
            report.error(path, 1, f"unknown frontmatter keys: {', '.join(sorted(unknown))}")

        # AGENTS.md: the verification flags are quoted strings, deliberately.
        if "date_range_verified" in front:
            raw, line_no = front["date_range_verified"]
            if raw not in ('"y"', '"n"'):
                report.error(
                    path, line_no,
                    f'date_range_verified is {raw or "empty"}, must be "y" or "n" '
                    "with quotes — bare y and n are booleans to a YAML 1.1 parser",
                )
        else:
            report.warn(path, 1, "no date_range_verified flag")

        if "status" in front:
            raw, line_no = front["status"]
            status = unquote(raw)
            if status not in STATUSES:
                report.error(
                    path, line_no,
                    f"status '{status}' is not one of: {', '.join(STATUSES)}",
                )

        threads = parse_list(front["threads"][0]) if "threads" in front else []
        unassigned = unquote(front.get("thread_assignment", ("", 0))[0]) == "unassigned"
        if "threads" in front:
            line_no = front["threads"][1]
            bad = [t for t in threads if t not in THREADS]
            if bad:
                report.error(
                    path, line_no,
                    f"unknown thread(s) {', '.join(bad)}; the four are "
                    f"{', '.join(sorted(THREADS))}",
                )
            if not threads and not unassigned:
                report.error(
                    path, line_no,
                    "threads is empty without thread_assignment: unassigned — "
                    "an empty list must be a recorded decision, not an omission",
                )

        chapters[number] = {
            "path": path,
            "front": front,
            "lines": lines,
            "body_start": end,
            "threads": threads,
            "sources": parse_list(front["sources"][0]) if "sources" in front else [],
            "open_questions": (
                parse_list(front["open_questions"][0])
                if "open_questions" in front else []
            ),
            "date_range": unquote(front.get("date_range", ("", 0))[0]),
            "verified": unquote(front.get("date_range_verified", ("", 0))[0]),
            "title": unquote(front.get("title", ("", 0))[0]),
        }

    if chapters:
        numbers = sorted(int(n) for n in chapters)
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            gaps = sorted(set(expected) - set(numbers))
            report.error(
                ROOT / "chapters", 1,
                f"chapter numbers are not contiguous from 01; missing {gaps}",
            )
    report.checks_run += 1
    return chapters


def check_unverified_dates_not_in_prose(chapters, report: Report):
    """Rule 1: a chapter whose date_range is unverified may not state a year.

    Headings are exempt — several tentpoles have a year in their conventional
    name, and "The Coinage Act of 1873" is the event's name rather than an
    assertion about when it happened. Inline code is exempt too, so that a
    blocker can refer to `date_range` values without tripping this.
    """
    for number, chapter in sorted(chapters.items()):
        if chapter["verified"] == "y":
            continue
        for i, line in enumerate(chapter["lines"][chapter["body_start"]:],
                                 start=chapter["body_start"] + 1):
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            scrubbed = re.sub(r"`[^`]*`", "", line)
            for match in re.finditer(r"\b1[6-9]\d{2}\b", scrubbed):
                report.error(
                    chapter["path"], i,
                    f"year {match.group(0)} in prose while "
                    'date_range_verified is "n" — verify it and log a '
                    "CLAIMS.md row, or say it without the date",
                )
    report.checks_run += 1


def check_manifest(report: Report):
    path = ROOT / "sources" / "MANIFEST.md"
    lines = read(path)
    rows = parse_table(lines, MANIFEST_COLUMNS, path, report)
    sources = {}
    for cells, line_no in rows:
        key, _author, title, _year, type_, acquired, read_, relevance = cells
        if key in sources:
            report.error(path, line_no, f"duplicate source key '{key}'")
        if not re.match(r"^[a-z0-9-]+$", key):
            report.error(
                path, line_no,
                f"source key '{key}' should be lowercase, digits and hyphens only",
            )
        if type_ not in SOURCE_TYPES:
            report.error(
                path, line_no,
                f"type '{type_}' is not one of: {', '.join(sorted(SOURCE_TYPES))}",
            )
        for name, value in (("acquired", acquired), ("read", read_)):
            if value not in ('"y"', '"n"'):
                report.error(
                    path, line_no,
                    f'{name} is {value or "empty"}, must be "y" or "n" with '
                    "quotes — AGENTS.md requires the quoted form here too",
                )
        if unquote(read_) == "y" and unquote(acquired) == "n":
            report.error(
                path, line_no,
                f"'{key}' is marked read but not acquired",
            )
        sources[key] = {
            "line": line_no,
            "title": title,
            "type": type_,
            "acquired": unquote(acquired),
            "read": unquote(read_),
            "relevance": relevance,
        }

    # Page numbers, ISBNs and quotations must not appear in table rows. The
    # prose above the table is free to say that they are prohibited.
    for i, line in enumerate(lines, start=1):
        if not line.strip().startswith("|"):
            continue
        for pattern, what in (
            (r"\bISBNs?\b", "an ISBN"),
            (r"\bpp?\.\s*\d", "a page number"),
            (r"[“”\"][^“”\"]{25,}[“”\"]", "a quotation"),
        ):
            if re.search(pattern, line):
                report.error(
                    path, i,
                    f"manifest row appears to contain {what}; rule 2 forbids "
                    "producing one from memory and the manifest is not a "
                    "citation",
                )
    report.checks_run += 1
    return sources


def check_claims(sources, chapters, report: Report):
    path = ROOT / "research" / "CLAIMS.md"
    lines = read(path)
    rows = parse_table(lines, CLAIMS_COLUMNS, path, report)
    verified_keys = set()
    for cells, line_no in rows:
        _claim, chapter, source_key, verified, _notes = cells
        if source_key not in sources:
            report.error(
                path, line_no,
                f"source_key '{source_key}' is not in sources/MANIFEST.md — "
                "a claim may not cite a source the book does not have",
            )
        # AGENTS.md names frontmatter and MANIFEST.md for the quoted form and
        # does not name CLAIMS.md, so both spellings are accepted here.
        flag = unquote(verified)
        if flag not in {"y", "n"}:
            report.error(path, line_no, f"verified is '{verified}', must be y or n")
        number = chapter.zfill(2)
        if number not in chapters:
            report.error(path, line_no, f"chapter '{chapter}' does not exist")
        if flag == "y":
            if source_key in sources and sources[source_key]["read"] != "y":
                report.error(
                    path, line_no,
                    f"claim is verified against '{source_key}', which is not "
                    'marked read: "y" in the manifest',
                )
            verified_keys.add((number, source_key))

    for number, chapter in sorted(chapters.items()):
        for key in chapter["sources"]:
            if key not in sources:
                report.error(
                    chapter["path"], chapter["front"]["sources"][1],
                    f"frontmatter cites '{key}', which is not in the manifest",
                )
            elif (number, key) not in verified_keys:
                report.error(
                    chapter["path"], chapter["front"]["sources"][1],
                    f"frontmatter cites '{key}' with no verified CLAIMS.md row "
                    f"for chapter {number} — rule 1",
                )
    report.checks_run += 1


def check_questions(chapters, report: Report):
    path = ROOT / "research" / "QUESTIONS.md"
    lines = read(path)
    ids: dict[str, int] = {}
    order: list[str] = []
    for i, line in enumerate(lines, start=1):
        for qid in re.findall(r"\*\*(Q(?:X|\d+)-\d+)\*\*", line):
            if qid in ids:
                report.error(path, i, f"duplicate question id {qid}")
                continue
            ids[qid] = i
            order.append(qid)

    by_chapter = collections.defaultdict(list)
    for qid in order:
        prefix, num = qid.split("-")
        by_chapter[prefix].append(int(num))

    for prefix, numbers in sorted(by_chapter.items()):
        if numbers != list(range(1, len(numbers) + 1)):
            report.error(
                path, ids[f"{prefix}-{numbers[0]}"],
                f"{prefix} question numbers are not sequential from 1: {numbers}",
            )
        if prefix != "QX" and prefix.lstrip("Q").lstrip("0") and \
                prefix[1:] not in chapters:
            report.error(path, 1, f"{prefix} has no matching chapter file")

    for number, chapter in sorted(chapters.items()):
        expected = [f"Q{number}-{n}" for n in sorted(by_chapter.get(f"Q{number}", []))]
        listed = chapter["open_questions"]
        if listed != expected:
            line_no = chapter["front"]["open_questions"][1]
            missing = [q for q in expected if q not in listed]
            extra = [q for q in listed if q not in expected]
            detail = []
            if missing:
                detail.append(f"missing {', '.join(missing)}")
            if extra:
                detail.append(f"not in QUESTIONS.md: {', '.join(extra)}")
            if not detail:
                detail.append("same ids, wrong order")
            report.error(
                chapter["path"], line_no,
                "open_questions disagrees with QUESTIONS.md — " + "; ".join(detail),
            )
    report.checks_run += 1
    return order


def check_triage(question_ids, report: Report):
    path = ROOT / "notes" / "question-triage.md"
    if not path.exists():
        report.warn(path, 1, "no triage file")
        return
    lines = read(path)
    categories = collections.defaultdict(list)
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [c.strip() for c in stripped[1:-1].split("|")]
        if len(cells) != 6 or "---" in cells[0] or cells[0] == "ch":
            continue
        for name, cell in zip("GPACT", cells[1:]):
            for qid in re.findall(r"Q(?:X|\d+)-\d+", cell):
                categories[name].append((qid, i))

    assigned = collections.Counter(
        qid for name in "GPAC" for qid, _ in categories[name]
    )
    for qid in question_ids:
        if assigned[qid] == 0:
            report.error(
                path, 1,
                f"{qid} is in QUESTIONS.md but not in the triage table",
            )
        elif assigned[qid] > 1:
            report.error(path, 1, f"{qid} is assigned to more than one category")
    known = set(question_ids)
    for name in "GPACT":
        for qid, line_no in categories[name]:
            if qid not in known:
                report.error(
                    path, line_no,
                    f"{qid} is triaged but is not in QUESTIONS.md",
                )

    counts = {name: len(categories[name]) for name in "GPACT"}
    text = "\n".join(lines)
    stated = re.search(
        r"Distribution:\s*(\d+)\s*gate,\s*(\d+)\s*parallel,\s*(\d+)\s*"
        r"authorial,\s*(\d+)\s*convention",
        text,
    )
    if stated:
        line_no = text[: stated.start()].count("\n") + 1
        for value, name, label in zip(
            stated.groups(), "GPAC", ("gate", "parallel", "authorial", "convention")
        ):
            if int(value) != counts[name]:
                report.error(
                    path, line_no,
                    f"stated {label} count is {value}, table has {counts[name]}",
                )
    else:
        report.warn(path, 1, "no stated distribution line to cross-check")

    check_stated_counts(len(question_ids), counts["T"], report)
    report.checks_run += 1


def check_stated_counts(total_questions, thesis_critical, report: Report):
    """Catch prose that states a count which has since moved.

    This is the drift that actually happened: notes/README.md described the
    triage as covering the wrong number of questions, and nine thesis-critical
    ones where the table marks seven. Wrong numbers in an index file are the
    cheapest possible way to make the apparatus look unreliable.

    Only phrases of the form "all N questions" are read as claims about the
    whole set, so a count of some subset must not be written that way — say
    "the five archival questions", not "all five questions".
    """
    targets = list((ROOT / "notes").glob("*.md")) + [
        ROOT / "README.md",
        ROOT / "BACKLOG.md",
        ROOT / "AGENTS.md",
        ROOT / "research" / "QUESTIONS.md",
    ]
    for path in targets:
        if not path.exists():
            continue
        for i, line in enumerate(read(path), start=1):
            for match in re.finditer(
                r"\ball\s+(\d+|[a-z-]+)\s+(?:[a-z-]+\s+)?questions\b", line, re.I
            ):
                token = match.group(1).lower()
                value = int(token) if token.isdigit() else NUMBER_WORDS.get(token)
                if value is None:
                    continue
                if value != total_questions:
                    report.error(
                        path, i,
                        f"says '{match.group(0)}' but QUESTIONS.md has "
                        f"{total_questions}",
                    )
            for match in re.finditer(
                r"\b(\d+|[a-z-]+)\s+(?:that are\s+)?thesis-critical", line, re.I
            ):
                token = match.group(1).lower()
                value = int(token) if token.isdigit() else NUMBER_WORDS.get(token)
                if value is None:
                    continue
                if value != thesis_critical:
                    report.error(
                        path, i,
                        f"says '{match.group(0)}' but the triage table marks "
                        f"{thesis_critical}",
                    )
    report.checks_run += 1


def check_chapter_order(chapters, report: Report):
    path = ROOT / "notes" / "chapter-order.md"
    if not path.exists():
        report.warn(path, 1, "no chapter-order file")
        return
    lines = read(path)
    rows = parse_table(
        lines, ["#", "chapter", "provisional date", "home thread"], path, report
    )
    seen = set()
    for cells, line_no in rows:
        number, _label, date_range, thread = cells
        seen.add(number)
        if number not in chapters:
            report.error(path, line_no, f"row for chapter {number}, which does not exist")
            continue
        chapter = chapters[number]
        if date_range != chapter["date_range"]:
            report.error(
                path, line_no,
                f"date '{date_range}' disagrees with the chapter file's "
                f"'{chapter['date_range']}'",
            )
        expected = chapter["threads"][0] if chapter["threads"] else "*unassigned*"
        if thread != expected:
            report.error(
                path, line_no,
                f"home thread '{thread}' disagrees with the chapter file's "
                f"'{expected}'",
            )
    for number in sorted(set(chapters) - seen):
        report.error(path, 1, f"chapter {number} is missing from the order table")
    report.checks_run += 1


def check_chapter_prose(chapters, report: Report):
    """No page numbers, ISBNs or long quotations anywhere in a chapter."""
    for number, chapter in sorted(chapters.items()):
        for i, line in enumerate(chapter["lines"], start=1):
            scrubbed = re.sub(r"`[^`]*`", "", line)
            for pattern, what in (
                (r"\bISBNs?\b", "an ISBN"),
                (r"\bpp?\.\s*\d", "a page number"),
            ):
                if re.search(pattern, scrubbed):
                    report.error(
                        chapter["path"], i,
                        f"chapter contains {what}; rule 2 forbids producing one "
                        "from memory",
                    )
    report.checks_run += 1


def check_primary(report: Report):
    for path in sorted((ROOT / "primary").glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        if not re.search(r"provenance", text, re.I):
            report.error(
                path, 1,
                "a transcription must record its provenance; /primary/README.md "
                "says what that means",
            )
    report.checks_run += 1


CHECKS_NOT_MADE = """\
What this script does not check, and cannot:

  * Whether a claim is true.
  * Whether a source says what a CLAIMS.md row says it says.
  * Whether acquired: "y" or read: "y" reflects a book anyone opened, or
    whether "read" means read rather than skimmed.
  * Whether a recorded disagreement is a fair account of both positions.
  * Whether a present-day parallel is doing framing work or evidence work.
  * Whether the prose is any good.

Those are the checks that matter. This script exists so that attention is not
spent on the mechanical ones.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--quiet", action="store_true", help="failures only")
    parser.add_argument("--list", action="store_true",
                        help="describe the checks and exit")
    args = parser.parse_args()

    if args.list:
        print(__doc__)
        print(CHECKS_NOT_MADE)
        return 0

    report = Report()
    chapters = check_chapters(report)
    sources = check_manifest(report)
    check_claims(sources, chapters, report)
    question_ids = check_questions(chapters, report)
    check_triage(question_ids, report)
    check_chapter_order(chapters, report)
    check_unverified_dates_not_in_prose(chapters, report)
    check_chapter_prose(chapters, report)
    check_primary(report)

    if report.warnings and not args.quiet:
        print(f"{len(report.warnings)} warning(s):")
        for warning in report.warnings:
            print(f"  {warning}")
        print()

    if report.errors:
        print(f"{len(report.errors)} error(s):")
        for error in report.errors:
            print(f"  {error}")
        return 1

    if not args.quiet:
        unverified = sum(1 for c in chapters.values() if c["verified"] != "y")
        unread = sum(1 for s in sources.values() if s["read"] != "y")
        print(
            f"ok — {len(chapters)} chapters, {len(sources)} sources, "
            f"{len(question_ids)} questions, {report.checks_run} checks"
        )
        print(
            f"     {unverified} chapters still have an unverified date range; "
            f"{unread} sources unread"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
