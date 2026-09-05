# CLAIMS

Every specific assertion in `/chapters` needs a row here, and no assertion may
appear in a chapter unless its row reads `verified: y`. See rule 1 in
`AGENTS.md`.

This file is the book's spine. If it is thin, the book is thin, regardless of
how much prose exists.

## How to fill a row

- **claim** — one assertion, stated as it will appear to a reader. Not a topic.
  "The act passed in February" is a claim; "the Coinage Act" is not. Split
  compound claims into separate rows, because they can fail separately.
- **chapter** — the chapter number the claim appears in. A claim used in two
  chapters gets two rows, since each use can drift.
- **source_key** — a key from `/sources/MANIFEST.md`. Never a source that is
  not in the manifest. Never a page number invented here.
- **verified** — `y` only when a human has looked at the source with their own
  eyes and seen the claim in it. Not `y` because the claim is well known, not
  `y` because three websites agree, not `y` because it sounds right.
- **notes** — where in the source, whether other sources disagree, and what
  the claim is load-bearing for. If historians disagree, that goes here and
  the disagreement gets recorded in the chapter too, per rule 4.

Rows stay in the file after they fail verification. A claim that turned out to
be wrong is worth more than a blank, because it stops the same wrong claim from
being reintroduced later.

## Ledger

| claim | chapter | source_key | verified | notes |
| --- | --- | --- | --- | --- |
| _(worked example — not a verified claim, do not cite)_ The Coinage Act of 1873 ended free coinage of the standard silver dollar, so that a holder of silver bullion could no longer bring it to the Mint to be struck into legal-tender dollars. | 07 | friedman-schwartz-monetary-history | n | Shows the granularity a row needs: one mechanism, stated the way a reader will meet it, not "the Coinage Act demonetised silver" — which bundles a mechanism, an intent, and a consequence into one unfalsifiable phrase. Cannot be marked `y`: source is `acquired: n`. Two further rows will be needed before chapter 07 can make its argument, one for whether contemporaries understood the provision (contested — see rule 4) and one for the act's effect on the silver price. See QUESTIONS.md Q07. |
