# BACKLOG

The task ledger. Every item has an owner, a reason, and a condition that makes
it done.

This file does not re-sort the research questions — `/notes/question-triage.md`
does that, by what each question blocks, and it is authoritative for research
sequence. The backlog is the wider list: tooling, repository hygiene,
acquisition, and the loose ends currently sitting in prose inside the notes
files where nothing will trip over them.

## The constraint that shapes this list

An agent working this repository overnight cannot do the research. Rule 2
forbids producing citations or findings from recall, and no source in
`/sources/MANIFEST.md` is acquired. That is not a gap in the plan; it is the
plan working as designed. What follows is therefore sorted by **who can
actually move it**, because a backlog that mixes "run this script" with "read
this book" and "decide this" produces the illusion of progress.

| owner | meaning |
| --- | --- |
| **agent** | Mechanical or structural. No source and no authorial judgment needed. Can be done unattended. |
| **author** | A decision only the author can make. An agent may prepare the options; it may not choose. |
| **reading** | Needs a source in hand. Blocked until acquisition. |
| **archive** | Needs a repository, a database, a translation, or correspondence. Longest lead time in the project. |

## Ready now — agent

- [x] **B-01 — Repository integrity checks.** `tools/check.py`. The rules in
      `AGENTS.md` are currently enforced by good intentions, and the scaffolding
      pass proved that insufficient: a `CLAIMS.md` row cited a `source_key`
      that was not in the manifest, caught by a hand-run scan that nobody was
      obliged to run. Thirteen checks now cover what a script can make binding,
      and `--list` prints the full account including what it deliberately
      cannot check — whether a claim is true, whether a source says what a row
      says it says, whether `read: "y"` means anyone opened the book. Those are
      human checks and they are the ones that matter; the script exists so that
      attention is not spent on the mechanical ones.
      **Done when:** `python3 tools/check.py` exits non-zero on a violation and
      reports every failure with a file and line — and `tools/test_check.py`
      proves it, by breaking the repository thirty ways and confirming each
      breakage is caught. It found two errors of mine while being built: a
      wrong source total in this file, and a first version of the count check
      that would not have caught the drift it was written for.

- [x] **B-02 — Sync `notes/README.md` counts.** It described
      `question-triage.md` as covering one question fewer than exists and nine
      thesis-critical questions where the table marks seven. The triage file
      itself was correct and internally exact — every question assigned once,
      the stated distribution matching the table — so only the index file was
      wrong. Small, but this is the file a new session reads first, and a wrong
      number there is the cheapest possible way to make the whole apparatus
      look unreliable.
      **Done when:** the counts match, and `check.py` verifies them so the next
      drift is caught rather than noticed.

- [x] **B-03 — Quote the `y`/`n` flags in `MANIFEST.md`.** `AGENTS.md` now
      requires quoted `"y"` and `"n"` "here and in `/sources/MANIFEST.md`", and
      all 76 manifest rows carry bare `n`. The binding rule and the file
      disagree, which makes the rule advisory in practice. Complying is not the
      same as amending, so this needs no authorial ruling — see B-14 for the
      part that does.
      **Done when:** no manifest row carries a bare flag, and `check.py`
      enforces it.

- [x] **B-04 — Populate every chapter's `open_questions` frontmatter.** All 20
      chapters carry `open_questions: []` while `QUESTIONS.md` holds 116
      chapter-specific questions. The field exists to make a chapter's blockers
      legible from the chapter, and leaving it empty means the only route from a
      chapter to its questions is prose in a drafting-blockers list.
      **Done when:** each chapter lists its own question IDs, and `check.py`
      fails if a chapter's list and `QUESTIONS.md` disagree — which turns
      closing a question into a two-file edit the tool polices.

- [x] **B-05 — Record the two unsourced money questions in the manifest's gaps
      section.** `question-triage.md` establishes that Q10-3 (the Vienna and
      Berlin side of the 1873 panic) and Q19-4 (who paid for the Afghan war)
      have nothing behind them in the bibliography, and notes that this belongs
      in `MANIFEST.md`'s own list of gaps, where it is currently absent. These
      are two of the four questions that decide whether the money thread leaves
      America, so the gap is load-bearing.
      **Done when:** the gaps section names both.

- [x] **B-06 — Number the spelling question.** `voice-and-shape.md` raises
      British versus American forms and `question-triage.md` says outright that
      it "is not yet a numbered question and should be". Ten of twenty
      chapters are American in subject and the repository is currently written
      in British forms throughout.
      **Done when:** it exists as **QX-6**, is placed in the triage table, and
      every count that moves has moved with it.

- [x] **B-07 — Source acquisition worksheet.** `/sources/ACQUISITION.md`. The
      manifest records what the book needs and says nothing about how any of it
      arrives, so the first real research session would otherwise begin with an
      unsorted list of seventy-six things. Routes are a search order derived
      from the manifest's own `year` and `type` columns, so they inherit that
      column's unverified status: the worksheet is a plan for acquisition, never
      evidence about a source, and "try a digital library first" is not a
      determination that a text is out of copyright.
      **Done when:** every manifest key appears exactly once with a route, and
      `check.py` enforces that — a plan that silently loses a source is worse
      than no plan, because the missing entry looks acquired-and-forgotten
      rather than never-ordered.
      **Outcome:** the twelve primary texts are the whole of the cheap first
      push. No monograph in the manifest predates 1930, so `question-triage.md`
      cluster 2 and the public-domain route turn out to be the same list.
      Nineteen monographs fall in the awkward 1930–1989 band where a library is
      the likely route and the lead time is longest; six of those are in the
      first fifteen books, so they want ordering now even though they are read
      later.

- [x] **B-08 — A `status` ladder for chapters.** `AGENTS.md` says to move a
      chapter's `status` "onward" from `stub` without saying what the next rung
      is, so the field could not be validated and every chapter would have sat
      at `stub` until someone invented a vocabulary mid-draft. Proposed and
      documented in `README.md`, deliberately tied to verification rather than
      to word count: `stub` → `gates-closed` (every gate question answered) →
      `drafting` → `drafted` → `verified` (every assertion carries a
      `verified: "y"` row).
      **Done when:** the ladder is documented and `check.py` accepts only those
      values — done — **and B-14 has confirmed it.** Still open, because this is
      an agent proposal about the author's process: the vocabulary is agent
      work, the adoption is not.

## Decided — author

The author ruled on all seven of these in one pass. Each entry records the
ruling and what was changed, because a decision that is not written down gets
relitigated by the next session. The rulings themselves are recorded as D-4
through D-10 in `thesis.md`.

- [x] **B-09 — does the Impressionist chapter exist, and in which thread?**
      Decided: it does not. The material is rolled in as support and colour
      elsewhere. The chapter file is deleted, chapters 12 through 21 are
      renumbered 11 through 20, and the exhibition's surviving questions moved
      to the cross-cutting block as QX-8 through QX-12 with QX-7 added to ask
      which chapter absorbs them. Two questions were retired rather than moved:
      the thread assignment, which the ruling answers, and the thesis-critical
      test of whether the chapter had a sourced link to the machines thread,
      which mattered only while the chapter's existence was in question. The
      underlying question survives as QX-12, demoted from gate to parallel.
      Thesis-critical questions fall from seven to six.

      The cut had one consequence worth flagging back: the exhibition was the
      only tentpole dated 1874, so the sequence now runs from four 1873
      chapters straight to 1876 and no tentpole falls in 1874 or 1875. That is
      recorded as QX-13 with two candidate remedies in
      `notes/chapter-order.md`, and it is a new author decision rather than a
      settled one.

- [ ] **B-10 — D-3b: hold or resolve the first-person test.**
      `notes/thesis.md` defers this until chapters 11 and 07 exist, which is
      the right call. Listed so that it is a live deferral rather than a
      forgotten one, and so nobody drafts under a ban that was never imposed.

- [x] **B-11 — the inherited first person in `AGENTS.md`.** Decided: remove
      it. The illustration now reads "the sources this book could reach". Note
      that this was not a straight deletion — "the sources available" would
      have removed the first person and quietly upgraded a claim about one
      research process into a claim about the world's archives, which is a
      bigger assertion than the original and an unverifiable one. The rule now
      says so explicitly, so the next drafter does not make that trade by
      accident. Does not pre-empt B-10, which is about the book's prose rather
      than about one sentence in a rules file.

- [x] **B-12 — rule 1 versus interpretation.** Decided: take it, with edits.
      The section is in `AGENTS.md` under "Rows are for assertions of fact,
      not for reasoning." Two edits to what `voice-and-shape.md` proposed.
      First, the proposed text listed "sequence" among the things needing no
      row. In a chronological history that is a hole big enough to drive an
      unsourced narrative through — the order in which things happened is a
      matter of fact and rule 1 covers it — so "sequence" is gone and
      "emphasis, structure" took its place. Second, an anti-loophole
      paragraph: if a sentence could be checked against a source it is an
      assertion of fact however it is dressed. Without that, the section is a
      licence to relabel claims as interpretation, which would make it a net
      loss over having no section at all.

- [x] **B-13 — spelling convention (QX-6).** Decided: American forms. Swept
      across the repository in one pass. QX-6 is answered rather than open, and
      the question is retained in `QUESTIONS.md` with the ruling recorded, since
      a decided convention still needs to be findable by whoever is drafting.
      What the sweep did not touch: quotations, titles of works, and quoted
      period usage, which keep their own spelling and always will.

- [x] **B-14 — B-08's status ladder.** Confirmed. The ladder is ratified rather
      than proposed, and `check.py` enforces the vocabulary.

- [x] **B-22 — whether `tools/check.py` becomes a rule.** Required, for now.
      Step 8 of the working procedure in `AGENTS.md`: run it, leave it passing,
      before every commit. Recorded as provisional in D-9, since the honest
      case for it rests on the script staying fast and staying free of
      dependencies, and a rule requiring a slow or fragile tool would be worse
      than no rule.

- [x] **B-23 — whether `CLAIMS.md`'s `verified` column takes quotes too.**
      Decided: quote it, for uniformity. Done, and `check.py` now requires the
      quoted form there rather than accepting either. It caused no other
      issues; the ledger has one example row, so the change was a single cell.
      The reasoning in the original entry still stands — the YAML argument
      genuinely does not apply to a table cell — so the rule now rests on
      uniformity, which is a weaker but sufficient reason, and `AGENTS.md`
      names all three locations rather than implying a parser-driven one.

## Blocked on reading

Every item here is waiting on the same thing: books in hand. `check.py` will
refuse to let any of it reach a chapter early, which is the point.

- [ ] **B-15 — Batch-verify all 20 `date_range` values.** The single
      highest-leverage research action available, and `question-triage.md`
      cluster 1 explains why: one pass against two or three reliable
      chronologies flips 20 flags, closes the first drafting blocker in all 20
      chapters, and settles three of the open structural problems in
      `chapter-order.md` — whether Darwin really precedes Chicago, whether the
      famine's move earlier survives its actual dates, and whether chapter 19
      runs past the decade. Needs a source, so it is not agent work; it is the
      first thing to do with one.
      **Done when:** 20 `CLAIMS.md` rows exist, 20 flags read `"y"`, and
      `chapter-order.md` records what the verification changed.

- [ ] **B-16 — Acquire and transcribe the out-of-copyright primary texts.**
      Cluster 2: the Coinage Act and Comstock Act texts, `darwin-descent`,
      `butler-erewhon`, `joseph-indian-view`, `howard-nez-perce-joseph`, the
      two treaty texts, the Specie Resumption Act. Unblocks every rule 5
      dependency at once and takes `/primary` from empty to useful.
      Depends on B-07 for routes.

- [ ] **B-17 — The money-crosses-borders cluster: Q01-3, Q07-5, Q10-3,
      Q19-4.** Four questions in four chapters that are one question in four
      costumes, and the only cluster that can change the book's architecture:
      the money thread is five American chapters, the empire thread five
      non-American ones, so the threads currently partition by geography at
      exactly the point the connected-decade argument needs them not to.
      Q01-3 and Q07-5 can be read as soon as `flandreau-glitter-of-gold` and
      `eichengreen-globalizing-capital` arrive. Q10-3 and Q19-4 need a source
      to be *found* first — see B-18.
      **Done when:** all four are answered or recorded as null, and the thread
      structure is decided on the result rather than around it.

- [ ] **B-18 — Find sources for Q10-3 and Q19-4.** A bibliography search, not
      a reading task, and it should start early enough that a null result is
      still actionable: the two questions that would carry the money thread
      furthest from America are the two with nothing behind them. Q10-3 wants
      the Vienna and Berlin events of 1873 treated as part of the same crisis;
      Q19-4 wants war finance, and all three chapter 19 entries are military or
      narrative history.

- [ ] **B-19 — QX-5 and the periodization argument.** Now introduction
      material rather than a test of the premise, per `thesis.md`, but it feeds
      the argument the book opens with, so it is not optional. Wants the
      history of the period labels themselves — when "Gilded Age" came into use
      and how the literature carved the decade in two.

- [ ] **B-20 — Q04-4 and Q04-5 together: what chapter 04 argues.** Whether
      Erewhon was read in the 1870s, and what its documented later reception
      is. Between them these decide whether the chapter's claim is influence or
      anticipation, whether chapters 04 and 06 merge, and whether the machines
      thread spends its one present-day passage here. Q04-5's three recalled
      claims — the Dune name, Turing, Orwell — each need their own source and
      none may be used until sourced.

## Blocked on archives

- [ ] **B-21 — Open the five long-lead enquiries: Q09-5, Q13-6, Q16-6, Q17-6,
      Q19-5.** Black accounts of Colfax, Indian-authored accounts of the
      famine, strikers' own words, Nez Perce accounts, Afghan-side sources.
      These want repositories, databases, translation, and in some cases a
      reply from someone whose response time nobody controls.
      `question-triage.md` is right that they have the longest lead time in the
      project **and** are the likeliest to be quietly dropped, because each can
      be finessed with a sentence about the limits of the record. Starting them
      late means the honest gap becomes the only available option rather than
      the true one.
      **Done when:** five enquiries are open, with dates, and a note per
      enquiry recording what was asked and of whom.

## Structural questions with no owner yet

Neither is a task. Both are consequences of the current chapter list that will
have to be faced, and both are recorded here so they are not rediscovered
late.

- **The empty middle of the decade.** Four tentpoles in 1873, one in 1874, none
  in 1875, four in 1876. A book about the 1870s has a two-year hole in its
  middle with a pile-up either side of it. Either something belongs in 1875, or
  the book should say why the decade went quiet — and if that holds, it is an
  unusually good chapter for a book about installation. Downstream of B-15,
  since the dates behind the observation are unverified.

- **Twenty tentpoles is still a lot.** `voice-and-shape.md`'s length budget forces
  five chapters to about 3,000 words, and a 3,000-word chapter is a section that
  has been promoted. Worth asking per chapter whether it is a chapter. Any slot
  that opens has two claimants already: the 1875 gap, and a European money
  chapter if B-17 comes back strong.

## Not on this list, deliberately

**Drafting.** Chapters 11 and 07 are where the voice gets found, per
`voice-and-shape.md`, and both sit behind their gate questions. Nothing in the
repository is closer to draftable than it was, and an agent that produced a
chapter tonight would be producing exactly the fluent unsourced prose the
apparatus exists to prevent.

**Anything that closes a question.** Questions in this repository were written
so they cannot be closed by remembering something. An overnight agent has only
recall. The two facts sit together deliberately.
