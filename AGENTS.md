# AGENTS.md

Rules for every session in this repository, human or agent. These are binding,
not advisory. They exist because the author has a BA in history, not a PhD, and
intends to publish a book that a specialist could not embarrass. An agent that
produces fluent unsourced prose here has actively damaged the project, because
unsourced prose that reads well is harder to catch later than an obvious gap.

If a rule below blocks you from finishing a task, the rule wins. Stop and
record the obstacle in `/research/QUESTIONS.md`. A smaller true book is the
goal; a larger plausible one is the failure mode.

## The rules

1. **Never assert a date, figure, name, or quotation in `/chapters` that does
   not have a `source_key` in `/research/CLAIMS.md` marked `verified: y`.**
   This covers everything specific: dates, counts, prices, distances, statute
   numbers, titles, the spelling of a person's name. If it could be wrong, it
   needs a row.

2. **Never produce a citation, page number, or quotation from memory.** Not a
   page number, not a chapter number, not an archive box, not a "as Foner puts
   it." If a citation is needed and the source is not in `/sources`, add an
   entry to `/research/QUESTIONS.md` instead and leave the gap visible in the
   draft. A missing citation is a task. A fabricated one is a retraction.

3. **Unverified material goes in `/notes` or `/research`, never in
   `/chapters`.** Recall, hunch, inference, and half-memory are all legitimate
   research inputs and all belong outside `/chapters`. Moving something into
   `/chapters` is an assertion that it has cleared rule 1.

4. **Where historians disagree, record the disagreement rather than resolving
   it silently.** Name the positions, name who holds them, and say what would
   settle it. Choosing the majority view without saying you chose is the same
   failure as choosing the minority view without saying so. "Historians
   disagree" with no names attached is not a record of a disagreement.

5. **Prefer primary text pasted into `/primary` over paraphrase from recall.**
   If a primary source is quoted or characterised, transcribe the passage into
   `/primary` first, with its provenance, and work from the transcription.
   Paraphrase drifts, and drift in a paraphrase is invisible.

6. **Flag presentism.** Parallels to the present are the book's hook and are
   welcome. They are framing, never evidence. A parallel may not be used to
   support a claim about the 1870s, and any passage that leans on one is
   marked so it can be reviewed as rhetoric rather than read as argument.

## What follows from the rules

**Frontmatter dates are provisional.** Every chapter stub carries a
`date_range` for ordering, plus `date_range_verified: "n"`. Those ranges were
written from recall as scaffolding and are exactly the kind of thing rule 1
prohibits asserting. They may be used to sort files. They may not be restated
in prose, and they may not be trusted, until a `CLAIMS.md` row verifies them
and the flag flips to `"y"`.

**The `y`/`n` flags are quoted strings, deliberately.** Bare `y` and `n` are
boolean `true` and `false` to a YAML 1.1 parser and bare strings to some
others. A verification flag that changes meaning depending on what reads it is
not a verification flag. Write `"y"` and `"n"` with the quotes, here and in
`/sources/MANIFEST.md`.

**`threads[0]` is the home thread and is fixed by the author.** The four
threads are `money`, `race` (shorthand for race and citizenship), `machines`,
and `empire`. Each tentpole has one home thread, assigned by the author, and an
agent does not reassign it. Additional threads may be appended to the list only
when a sourced connection exists — not because a link seems plausible. One
chapter, the first Impressionist exhibition, has no home thread yet; leave it
empty until the author assigns one.

**Every number is a range until proven otherwise.** Nineteenth-century
mortality figures, casualty counts, crowd sizes, and unemployment rates are
reconstructions, not measurements. Give the range, the estimators, and the
reason they differ. A single round number in this book is a defect unless a
row explains why it is safe.

**Absence of a source is content.** "The Afghan side of this war is thinly
covered in the sources I can read" is a true and useful sentence. Writing
around the gap so the reader cannot see it is not.

## Working procedure

Before drafting in a chapter:

1. Read the chapter's `## Drafting blockers` section. It lists the traps
   specific to that chapter.
2. Read the chapter's questions in `/research/QUESTIONS.md`.
3. Confirm the sources you need are in `/sources/MANIFEST.md` with
   `acquired: y` and `read: y`. If not, that is the task instead.

While drafting:

4. Add a `CLAIMS.md` row before you write the sentence that depends on it, not
   after. A claim written first and sourced later is a claim that will ship
   unsourced.
5. Add the `source_key` to the chapter's `sources:` frontmatter list.
6. Move the chapter's `status` from `stub` onward only when its claims are
   verified rows, not when its prose is finished.

When you cannot verify something:

7. Write the question in `/research/QUESTIONS.md`, phrased as something a
   source must answer. Leave the gap in the draft marked and visible. Do not
   fill it with a hedge — "some accounts suggest" with no account named is a
   rule 2 violation wearing a disguise.

## Scope note

Bibliographic details in `/sources/MANIFEST.md` were seeded from recall. They
are pointers for acquisition, not citations, and rule 2 applies to them in
full: check every author, title, and year against the physical or scanned copy
before any of it reaches a footnote.
