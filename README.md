# eighteen-seventies

A trade history of the 1870s, for general readers.

**Working thesis:** The 1870s installed the operating system of the modern
world: money, race and citizenship, machines, empire.

**Four threads** run through the whole book rather than getting four separate
sections:

| thread | what it covers |
| --- | --- |
| **money** | the Coinage Act, Crédit Mobilier, the Panic of 1873, the Great Railroad Strike, specie resumption |
| **race and citizenship** | The Descent of Man, Colfax, the Comstock Act, the 1876 election and the Compromise of 1877, Chief Joseph's surrender |
| **machines** | Chicago rebuilt, Erewhon, Verne, Bell's telephone patent, Edison at Menlo Park |
| **empire** | the Franco-Prussian War, the Satsuma Rebellion, the Indian famine, Afghanistan, the Congress of Berlin |

The book is a straight chronology, 1870 to 1879. Twenty-one tentpole chapters
carry the sequence and smaller events fold in around them.

## Repository layout

| directory | contents | rule |
| --- | --- | --- |
| `/chapters` | The book. One file per tentpole, `NN-slug.md`. | Verified material only. |
| `/sources` | `MANIFEST.md`, the master bibliography with a citation key per work. | Nothing is cited unless it is here. |
| `/research` | `CLAIMS.md` and `QUESTIONS.md` — the verification ledger and the open questions. | The book's real engine. |
| `/primary` | Transcribed primary text, with provenance. | Transcription only, no commentary. |
| `/notes` | Thinking, conventions, structural decisions, historiography, loose ends. | Anything unverified goes here. |
| `/tools` | `check.py`, which enforces the mechanical half of the rules, and its tests. | Run it before you commit. |

`AGENTS.md` at the root holds the binding rules. Read it before writing
anything, and note that "binding" is meant literally rather than as
encouragement. `BACKLOG.md` holds the task list, sorted by who can move each
item, and points into `/notes/question-triage.md` for research sequence.

## The workflow

The whole method is one idea: **a claim gets verified before it gets written,
not after.** Reversing that order produces a manuscript full of confident
sentences whose sources nobody can reconstruct, which is the failure this
repository is built to prevent.

In practice, for any chapter:

1. **Read the chapter's questions.** `/research/QUESTIONS.md` lists, per
   chapter, what a source has to answer before the chapter can be drafted.
   Every question is phrased so that it cannot be closed by remembering
   something.
2. **Get the sources.** Find them in `/sources/MANIFEST.md`, acquire them,
   read them, and flip `acquired` and `read` to `"y"` — honestly. A source
   marked read that was skimmed is worse than one marked unread.
3. **Transcribe the primary text.** Anything to be quoted or characterised
   closely goes into `/primary` first, with provenance.
4. **Log the claims.** Each specific assertion becomes a row in
   `/research/CLAIMS.md` with its source key, marked `verified: y` only once
   someone has seen it in the source with their own eyes.
5. **Then write.** In `/chapters`, using only claims that have verified rows,
   and adding each source key to the chapter's frontmatter.
6. **Record what you could not settle.** Disagreements among historians get
   written into the chapter as disagreements. Gaps in the sources get stated
   plainly. Both are content, not embarrassments.
7. **Run the checks.** `python3 tools/check.py`, which needs nothing installed.

## What the checks do

`tools/check.py` enforces the half of the rules a script can reach: that every
`source_key` in `CLAIMS.md` exists in the manifest, that no chapter cites a
source without a verified row behind it, that a chapter with an unverified date
range does not state a year in its prose, that no page number or ISBN has
appeared anywhere, that the question list and its triage table agree, that
every reference to a question names one that exists, that the acquisition
worksheet covers the manifest exactly, and that counts stated in prose still
match what they count. `python3
tools/check.py --list` prints the full account, including what it cannot
check. `python3 tools/test_check.py` breaks the repository on purpose, one
thing at a time, and confirms the checker notices each one — a check that
passes because it never looks at anything is worse than no check.

It cannot tell whether a claim is true, whether a source says what a row says
it says, or whether `read: "y"` means anyone opened the book. Those checks are
human and they are the ones that matter. The script exists so that attention
is not spent on the mechanical ones.

## Chapter frontmatter

```yaml
---
title: "The Coinage Act of 1873"
date_range: "1873"
date_range_verified: "n"
threads: [money]
status: stub
sources: []
open_questions: []
---
```

`date_range_verified` matters more than it looks. The date ranges in every
stub were written from recall as scaffolding, which makes them exactly the
kind of thing the rules forbid asserting. They are there to sort files. They
do not go into prose until a source confirms them and the flag reads `"y"`.
The flags are quoted on purpose — bare `y` and `n` are booleans to some YAML
parsers and strings to others, and a flag that means different things to
different readers is worse than no flag.

`threads[0]` is the chapter's home thread, assigned by the author. Further
threads get appended only when a source supports the connection. One chapter,
the first Impressionist exhibition, has no home thread yet and its list is
deliberately empty.

`open_questions` lists the chapter's own question IDs from
`/research/QUESTIONS.md`. The two files have to agree, and `check.py` enforces
it, so closing a question is a two-file edit.

`status` moves along a ladder tied to verification rather than to word count:

| status | means |
| --- | --- |
| `stub` | No narrative content. Where every chapter is now. |
| `gates-closed` | Every gate question for the chapter is answered. See `/notes/question-triage.md`. |
| `drafting` | Prose exists and is incomplete. |
| `drafted` | Prose is complete. Says nothing about whether it is sourced. |
| `verified` | Every assertion in the chapter carries a `verified: "y"` row. |

That ladder is an agent proposal awaiting the author's confirmation — see
`BACKLOG.md` B-08 and B-14. `check.py` accepts only these five values, so
changing the vocabulary means changing one list in one file.

## Current state

Scaffolding only. Twenty-one chapter stubs with no narrative content, a
bibliography of works to acquire, and roughly a hundred open questions.
`CLAIMS.md` holds one illustrative row and no verified claims. `/primary` is
empty. Nothing has been read.

That is the intended starting position. The questions are the asset here — they
are what stands between a researched book and a fluent one.
