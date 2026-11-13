# ACQUISITION

How all 76 sources in `MANIFEST.md` are meant to arrive, and in what order.

The manifest records what the book needs and says nothing about how any of it
is obtained, so the first real research session would otherwise begin with an
unsorted list of seventy-six things. This file is the order to work in.

## What this is not

**It is not evidence about any source.** Nothing here is a finding. The routes
below are a *search order* — which shelf to try first — derived from the
manifest's own `year` and `type` columns, and that year column was seeded from
recall and is unverified. If a year is wrong, its route is wrong. Confirm the
book before trusting the route, never the reverse.

In particular, "try a digital library first" is not a determination that a text
is out of copyright. It means the stated year is old enough that a digital
library is the sensible first place to look, and that a paid copy is probably
unnecessary. The determination is made when the copy is in hand.

## The routes

| route | heuristic | why |
| --- | --- | --- |
| **D** | stated year before 1930 → try a digital library first | Old enough that scans are the likely path and the cost is zero. Every entry that qualifies is `type: primary`. |
| **N** | stated year 1990 or later → try a new copy first | Recent enough that purchase is likely the fastest route. |
| **L** | stated year 1930 to 1989 → try a library or interlibrary loan first | Old enough to be awkward to buy, recent enough to be in copyright. Long lead times, so order these early even when they are needed late. |

Mark progress in `MANIFEST.md` by flipping `acquired`, not here. This file is
the plan; the manifest is the record.

## Push 1 — the twelve primary texts

Route **D** throughout, and the cheapest useful work in the project.
`question-triage.md` cluster 2 makes the case: Q02-2, Q07-1, Q08-1, Q19-2 and
Q21-1 all say some version of "get the text into `/primary`", and one push
closes the category and unblocks every rule 5 dependency at once. It also takes
`/primary` from empty to useful, which changes what the next drafting session
is able to do.

Every entry here is a transcription target, so read `/primary/README.md` before
starting: provenance is recorded at the top of each file, and a transcription
whose provenance has silent gaps is not usable as evidence.

| key | stated year | chapter | note |
| --- | --- | --- | --- |
| coinage-act-1873-text | 1873 | 07 | Statute text. Q07-1 wants it section by section on silver. |
| comstock-act-text | 1873 | 08 | Formal title and statutory citation are themselves unconfirmed — Q08-1. |
| specie-resumption-act-text | 1875 | 21 | The act and the effective date are different things; Q21-1. |
| treaty-of-berlin-text | 1878 | 19 | Q19-2 needs this and the next entry together. |
| treaty-of-san-stefano-text | 1878 | 19 | The treaty Berlin replaced. |
| darwin-descent | 1871 | 02 | Editions differ (Q02-1); establish which one before transcribing. |
| butler-erewhon | 1872 | 04 | Revised after first publication; fix the edition first (Q04-1). |
| verne-tour-du-monde | 1873 | 06 | Serial and book are different texts, and the translation is an open convention (Q06-4). |
| joseph-indian-view | 1879 | 18 | Reaches us through an editor and a translator. A record of a transmission, and the provenance must say so. |
| howard-nez-perce-joseph | 1881 | 18 | The opposing commander's account. A source *about* a source, for Q18-1. |
| us-monetary-commission-report | 1877 | 07, 21 | Year and exact title both need confirming; the manifest says so. |
| naoroji-poverty-un-british-rule | 1901 | 14 | Published later, drawing on 1870s material. Date the data, not the book. |

## Push 2 — the first fifteen books

Not the fifteen most interesting. The fifteen that unblock the most.

**The chronology spine, for the 21 date verifications (B-15).** The five
entries the manifest's own relevance column marks as covering all four threads.
Cluster 1 wants "two or three reliable chronologies" for a single pass that
flips 21 flags and settles three structural questions in `chapter-order.md`;
these are the candidates already in the bibliography. QX-3 asks which synthetic
work is actually best per thread and is not yet answered, so treat this as the
available set rather than the right one.

- `white-republic-for-which-it-stands` — route N — the default first stop for every American chapter
- `osterhammel-transformation-of-the-world` — route N
- `bayly-birth-of-modern-world` — route N
- `hobsbawm-age-of-capital` — route L — note its period boundary falls mid-decade
- `hobsbawm-age-of-empire` — route L — the other half

**Money crosses borders, the readable half (B-17).** Q01-3 and Q07-5 are the
two of the four that already have sources aimed at them. Q10-3 and Q20-4 have
nothing, which is why B-18 is a search rather than a purchase.

- `flandreau-glitter-of-gold` — route N — aimed squarely at the indemnity-to-currency-reform link
- `eichengreen-globalizing-capital` — route N — the standard change in international frame
- `clark-iron-kingdom` — route N — the German side

**Chapter 12, where the voice gets found.** `voice-and-shape.md` argues for
drafting Bell's patent first: contained scope, a clean documented mechanism, a
live dispute that tests the rule 4 technique, and the book's second-most-famous
quotation to test quotation discipline on.

- `bruce-bell` — route L — order early, it is the oldest thing on this list
- `john-network-nation` — route N
- `shulman-telephone-gambit` — route N — a contested claim, to be cited as a position and not a finding

**Chapter 07, where the voice meets the Coinage Act.** The thesis chapter.

- `unger-greenback-era` — route L — covers the decade almost exactly
- `friedman-schwartz-monetary-history` — route L
- `weinstein-prelude-to-populism` — route L — central to the Crime of '73 dispute
- `barreyre-gold-and-freedom` — route N — joins the money and race threads directly

## Push 3 — the remaining forty-nine

No priority among these beyond their route. Order the route **L** entries when
Push 2 is ordered, since interlibrary loan sets the pace and these are needed
by chapters that are not drafted yet.

### Route L — try a library or interlibrary loan first

`ambirajan-classical-political-economy`, `anderson-eastern-question`,
`arnold-famine`, `bruce-1877-year-of-violence`, `clark-painting-of-modern-life`,
`foner-reconstruction`, `howard-franco-prussian-war`, `josephy-nez-perce`,
`rewald-history-of-impressionism`, `robson-road-to-kabul`,
`schivelbusch-railway-journey`, `sen-poverty-and-famines`,
`taylor-struggle-for-mastery`

### Route N — try a new copy first

`barfield-afghanistan`, `beisel-imperiled-innocents`, `bellesiles-1877`,
`blaise-time-lord`, `browne-darwin-power-of-place`, `cronon-natures-metropolis`,
`davis-late-victorian-holocausts`, `desmond-moore-darwins-sacred-cause`,
`glenny-the-balkans`, `gordon-rise-and-fall-american-growth`,
`greene-nez-perce-summer`, `hopkirk-great-game`, `horowitz-rereading-sex`,
`israel-edison`, `jansen-making-of-modern-japan`, `jonnes-empires-of-light`,
`keene-emperor-of-japan`, `keith-colfax-massacre`, `king-judgment-of-paris`,
`lane-day-freedom-died`, `lemann-redemption`, `miller-city-of-the-century`,
`ogle-global-transformation-of-time`, `ravina-last-samurai`,
`richardson-death-of-reconstruction`, `roe-private-lives-impressionists`,
`sawislak-smoldering-city`, `smith-urban-disorder`, `stowell-great-strikes-1877`,
`summers-era-of-good-stealings`, `summers-ordeal-of-the-reunion`,
`wawro-franco-prussian-war`, `werbel-lust-on-trial`, `west-last-indian-war`,
`white-railroaded`, `wicker-banking-panics`

## What no route reaches

Two categories of need are not on this list because no purchase closes them.

**The five long-lead archival enquiries** — Q09-5, Q14-6, Q17-6, Q18-6, Q20-5.
Black accounts of Colfax, Indian-authored accounts of the famine, strikers' own
words, Nez Perce accounts, Afghan-side sources. `MANIFEST.md` is explicit that
these are archival rather than bibliographic, and they want repositories,
databases, translation, and in some cases a reply from someone whose response
time nobody controls. They are the likeliest items in the project to be quietly
dropped, because each can be finessed with a sentence about the limits of the
record. Backlog item B-21; start them before Push 1, since they cost nothing to
open and everything to open late.

**The two questions with no source to acquire** — Q10-3 and Q20-4. The Vienna
and Berlin side of the 1873 panic, and who paid for the Afghan war. Nothing in
the bibliography addresses either, and they are two of the four questions that
decide whether the money thread leaves America. Backlog item B-18. Finding
those sources is prerequisite work for a structural decision, and it should
start early enough that a null result is still actionable.

**No journal articles and no newspapers appear anywhere above**, because none
are in the manifest. `MANIFEST.md` explains why: article citations need volume
and page details that cannot be produced from recall, and newspapers need a
database and a real search. Both are real acquisition work that this file
cannot yet sequence. See QX-4 and QX-5.
