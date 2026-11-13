# Erewhon: collating the 1872 and 1901 editions

A finding about two texts, with the method stated so it can be repeated or
overturned. Not verified by the author; `verified: "n"` in `CLAIMS.md`.

## Why this was done

Butler's preface to the revised edition says he added "about sixty" pages in
1901 to extend the book's copyright, and that he blended the new matter so
that "none but the best critics shall perceive at what places the gaps of
between thirty and forty years occur." Transcribed at
`/primary/1901-butler-preface-erewhon.md`.

Chapter 04 rests on the "Book of the Machines" as an 1872 document. If any of
those sixty pages fell there, the chapter's whole claim on the machines thread
would be reading 1901 back into 1872 — and Butler warns that you will not be
able to see the join.

## The two texts

| | 1872 | 1901 |
| --- | --- | --- |
| source | Internet Archive `erewhonoroverra00butl`, London: Trübner & Co., 1872, 268 leaves | Project Gutenberg eBook #1906 |
| form | OCR of page images | published transcription |
| sha256 | `fa60789ed3116c8c…` | `9b034d0990931fa4…` |
| words | 72,067 | 87,272 |

The 1901 figure includes Project Gutenberg's boilerplate and both prefaces, so
the gap of about 15,000 words is an upper bound on what Butler added. At the
page density of the 1872 printing that is roughly sixty pages, which agrees
with his own account.

## What changed: the chapter list

The 1872 contents and the 1901 contents differ in ways that locate the
additions.

| 1872 | 1901 |
| --- | --- |
| XX. The Colleges of Unreason | XXI. The Colleges of Unreason |
| — | **XXII. The Colleges of Unreason—Continued** |
| XXI. The Book of the Machines | XXIII. The Book of the Machines |
| XXII. The Machines—Continued | XXIV. The Machines—continued |
| XXIII. The Machines—concluded | XXV. The Machines—concluded |
| — | **XXVI. The Views of an Erewhonian Prophet concerning the Rights of Animals** |
| — | **XXVII. The Views of an Erewhonian Philosopher concerning the Rights of Vegetables** |
| XXIV. Escape | XXVIII. Escape |
| XXV. Conclusion | XXIX. Conclusion |

Three chapters are new in 1901, and the numbering also shifts by one earlier in
the book, so at least one further addition sits before chapter XVI. **None of
the new chapters is a machine chapter.** The three machine chapters appear in
both editions, in the same order, under the same titles.

## What did not change: the measurement

The machine chapters were extracted from each text and counted, with the
1872 running heads stripped, since OCR repeats them in the body.

- **1872, chapters XXI–XXIII: 10,144 words**
- **1901, chapters XXIII–XXV: 10,138 words**

A difference of six words, about one tenth of one per cent, which is within
what OCR noise alone would produce.

## Spot check of the text itself

Equal length does not prove identity: Butler could have rewritten without
changing the extent. The openings were therefore compared directly. They are
the same sentences:

> The writer commences:—"There was a time, when the earth was to all appearance utterly destitute both of animal and vegetable life, and when according to the opinion of our best philosophers it was simply a hot round ball with a crust gradually cooling…"

The 1872 printing sets "THE writer commences" with a drop capital, which the
OCR renders as `'THE` with a stray mark, and uses straight quotation marks
where Gutenberg's text uses curly ones. Those are typographic, not textual.

## What this establishes, and what it does not

**Establishes.** The sixty pages Butler added in 1901 did not go into the Book
of the Machines. Those chapters stand in the 1901 text at essentially their
1872 length, and they open with the same words. Chapter 04 may treat the
machine chapters as an 1872 document.

**Does not establish.** That the chapters are identical. A word count and a
matched opening rule out substantial addition; they do not rule out revision
of the kind that replaces a phrase with another of similar length, which is
exactly what Butler says he did elsewhere for "literary inelegancies". **Any
passage quoted in the book must still be quoted from the 1872 text**, which
is now in hand, and not from the 1901 one.

**A caution about the method.** The 1872 side of this comparison is OCR, used
here to count and to compare, not to quote. The word counts are therefore
approximate on that side. The conclusion is robust to that, because the
quantity being tested — roughly sixty added pages — is two orders of magnitude
larger than the error. A finding that depended on six words would not be.

## Consequence for the chapter list

`voice-and-shape.md` made the proposed merger of chapters 04 and 06
conditional on Q04-5: merge only if Erewhon's afterlife proves thin. This
finding does not settle that, but it strengthens the case for keeping 04
whole. The edition history is itself a story — a book revised to beat the
copyright clock, with the revision deliberately camouflaged by its author —
and it is a story about machines, publishing and law that sits comfortably on
the machines thread. That is a chapter's worth of material before the
afterlife question is even asked.
