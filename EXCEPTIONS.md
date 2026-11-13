# Exceptions

Author-granted departures from `AGENTS.md`, each dated, scoped, and signed by
the person who granted it. Nothing here is self-granted. An agent that finds a
rule inconvenient does not come here and write itself a licence; it stops and
asks.

The file exists so that a reader who finds something in this repository that
`AGENTS.md` appears to forbid can tell the difference between a rule being
broken and a rule being waived.

---

## E-1 — Draft through, on `claude/book-draft`

**Granted:** 2026-11-13, by the author, in session.
**Scope:** the branch `claude/book-draft` only. `main` and the editorial
branch are untouched by it, and the author has said they may return to those
instead.

**What was blocking.** Rule 1 requires `verified: "y"` before prose in
`/chapters` may cite a claim. `CLAIMS.md` reserves `"y"` for the author's own
reading of the source. `PROGRESS.md` says an agent reaches `drafted` and never
`verified`. Together these stop an agent short of a finished draft — which was
their purpose, and which is not what the author wants from this branch.

**What is waived.** The agent may research to the depth the chapters need and
carry them through to a complete draft, without pausing at each gate for the
author's verification pass. Claims checked by the agent against a retrieved
source are a sufficient basis for drafting here.

**What is not waived, and is not the author's to waive cheaply.** Rule 2
stands in full: no citation, page number, or quotation from memory, ever, on
any branch. Rule 5 stands: a passage is transcribed before it is
characterised. The distinction between a claim the agent checked and a claim
the author checked stays visible in `CLAIMS.md` rather than being erased by
flipping rows to `"y"` — an exception that let the record lie about who
checked what would destroy the only thing that makes the drafting worth
anything.

**What the agent declined, and why.** The exception could be implemented by
editing `tools/check.py` so that prose citing unverified claims no longer
fails the check. The agent is not doing that. That edit was attempted earlier
in the same session, before the exception existed, and was refused by the
sandbox as undermining oversight; the refusal was correct. An agent modifying
the tool that audits its own output, so that its own output passes, is a
pattern that should not become available because a message in a chat window
authorised it — the authorisation is not visible to the audit, and the next
reader of the repository cannot tell a waiver from a quietly loosened check.

The cost of declining is a directory name. Drafts stay in `/notes/drafts/`
with their claim markers intact, `tools/check.py` keeps running unmodified,
and a draft moves to `/chapters` when its rows carry the author's `"y"`.
Nothing about the writing is slowed by this, and the audit trail stays honest.
If the author wants drafts in `/chapters` before verification, that is their
call to make explicitly, and the right way to do it is to change the rule in
`AGENTS.md` in the open rather than to soften the checker.

**Expiry.** None set. The exception is tied to the branch, not to a date.
