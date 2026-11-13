# CLAIMS

Every specific assertion in `/chapters` needs a row here, and no assertion may
appear in a chapter unless its row reads `verified: y`. See rule 1 in
`AGENTS.md`.

This file is the book's spine. If it is thin, the book is thin, regardless of
how much prose exists.

## How to fill a row

- **id** — a stable handle, `C<chapter>-<nnn>`, e.g. `C12-003`. Assigned once
  and never reused, even after a row fails verification. This is what the
  prose in `/chapters` cites, so that any sentence in the book can be traced
  to the row that licenses it and from there to the source. Ids are permanent:
  renumbering them breaks every citation that points at them.
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

## How the prose cites a row

Every specific assertion in `/chapters` carries its claim id in square
brackets at the end of the sentence: `The patent issued on 7 March 1876
[C12-004].` `tools/check.py` reads those markers and fails if one points at a
row that does not exist, or at a row that is not `verified: "y"`, or if a
chapter's frontmatter cites a source no verified row uses.

The markers are working apparatus, not typography. `tools/reading_copy.py`
strips them to produce a clean reading text; the manuscript keeps them until
the book is typeset.

## Ledger

| id | claim | chapter | source_key | verified | notes |
| --- | --- | --- | --- | --- | --- |
| C07-000 | _(worked example — not a verified claim, do not cite)_ The Coinage Act of 1873 ended free coinage of the standard silver dollar, so that a holder of silver bullion could no longer bring it to the Mint to be struck into legal-tender dollars. | 07 | friedman-schwartz-monetary-history | n | Shows the granularity a row needs: one mechanism, stated the way a reader will meet it, not "the Coinage Act demonetised silver" — which bundles a mechanism, an intent, and a consequence into one unfalsifiable phrase. Cannot be marked `y`: source is `acquired: n`. Two further rows will be needed before chapter 07 can make its argument, one for whether contemporaries understood the provision (contested — see rule 4) and one for the act's effect on the silver price. See QUESTIONS.md Q07. |
| C12-001 | Letters Patent No. 174,465 is titled "Improvement in Telegraphy" and names Alexander Graham Bell, of Salem, Massachusetts, as the inventor. | 12 | bell-patent-174465 | n | Agent read it on the page image of specification p. 1, in the Patent Office heading. Author check: /primary/1876-bell-patent-174465.md, cached PDF p. 3. |
| C12-002 | The patent's specification states that the application was filed on 14 February 1876. | 12 | bell-patent-174465 | n | Agent read it on specification p. 1, in the line beginning "Specification forming part of Letters Patent No. 174,465". Author check: same page. |
| C12-003 | The patent is dated 7 March 1876. | 12 | bell-patent-174465 | n | Agent read it on specification p. 1 and on both drawing sheets, which carry "Patented March 7, 1876". |
| C12-004 | The patent's specification is signed and dated by Bell on 20 January 1876, twenty-five days before the application was filed. | 12 | bell-patent-174465 | n | Agent read it on specification p. 4: "In testimony whereof I have hereunto signed my name this 20th day of January, A. D. 1876." The interval is arithmetic from C12-002. Bears on Q12-3. Absent from the Google Patents OCR. |
| C12-005 | The patent carries five numbered claims. | 12 | bell-patent-174465 | n | Agent counted them on specification pp. 3-4. Transcribed in full at /primary/1876-bell-patent-174465-claims.md. |
| C12-006 | The patent's fifth claim covers the method of and apparatus for transmitting vocal or other sounds telegraphically by causing electrical undulations similar in form to the vibrations of the air accompanying the sound. | 12 | bell-patent-174465 | n | Agent read it on specification p. 4. Transcribed verbatim in the claims file. |
| C12-007 | The patent's fourth claim covers producing undulations in a continuous voltaic circuit by gradually increasing and diminishing the resistance of the circuit, or the power of the battery. It does not mention liquid. | 12 | bell-patent-174465 | n | Agent read it on specification p. 4. The absence of any reference to liquid is a reading of the claim as printed and matters for Q12-2. |
| C12-008 | The patent's specification offers mercury or other liquid as an instance of varying a circuit's resistance, the resistance falling as the conducting wire is immersed more deeply. | 12 | bell-patent-174465 | n | Agent read it on specification p. 2. Transcribed in full at /primary/1876-bell-patent-174465-undulatory.md. This is the passage the priority dispute turns on. |
| C12-009 | The patent recites an earlier patent granted to Bell on 6 April 1875, numbered 161,739. | 12 | bell-patent-174465 | n | Agent read it in the opening recitals, specification p. 1. The earlier patent has NOT been retrieved; this row establishes only that Bell's patent says so. |
| C12-010 | The witnesses to the patent's specification were Thomas E. Barry and P. D. Richards. | 12 | bell-patent-174465 | n | Agent read it on specification p. 4, set in type. The handwritten witness signatures on the two drawing sheets were not legible and are not claimed. |
| C12-011 | Bell's notebook entry headed 10 March 1876 records that the instrument shown in its Fig. I was constructed that morning and tried that evening. | 12 | bell-notebook-1875-1876 | n | Agent read it on the page image of notebook p. 40. Author check: /primary/1876-bell-notebook-march-10.md. |
| C12-012 | The transmitting instrument of 10 March 1876 was a liquid transmitter: a brass pipe and a platinum wire standing in liquid, beneath a mouthpiece. | 12 | bell-notebook-1875-1876 | n | Agent read the labelled diagram and the text identifying P as a brass pipe and W as the platinum wire, notebook p. 40. Connects the notebook to claim 4 and to C12-008. |
| C12-013 | Watson was stationed in one room with the receiving instrument, the transmitting instrument was in another, and the doors of both rooms were closed. | 12 | bell-notebook-1875-1876 | n | Agent read it on notebook p. 40. |
| C12-014 | Bell wrote the sentence he shouted as "Mr. Watson — Come here — I want to see you", with spaced dashes and a capitalised Come, and wrote it lower-case when recording Watson repeating it back. | 12 | bell-notebook-1875-1876 | n | Agent read both occurrences, notebook pp. 40-41. Neither familiar modern form matches. The single highest-risk quotation in the chapter after ch 18. |
| C12-015 | Watson came and declared that he had heard and understood what Bell said, and repeated the sentence back. | 12 | bell-notebook-1875-1876 | n | Agent read it on notebook p. 41. |
| C12-016 | With positions reversed and Watson reading an unknown passage, Bell could not follow the sense, making out only the words "to", "out" and "further" before one sentence came clearly. | 12 | bell-notebook-1875-1876 | n | Agent read it on notebook p. 41. The test is Bell's own control against knowing what to expect. |
| C12-017 | In the entry of 9 March 1876 Bell discounted his apparent hearing of counted numerals as possibly "fancy — as I knew beforehand what to expect". | 12 | bell-notebook-1875-1876 | n | Agent read it on notebook p. 39. Author check: /primary/1876-bell-notebook-march-08-12.md. |
| C12-018 | The 9 March 1876 apparatus used a membrane stretched across the bottom of a box, a cork at its centre supporting a wire that projected into water in a glass vessel, with a brass ribbon also immersed. | 12 | bell-notebook-1875-1876 | n | Agent read it on notebook p. 39. Establishes that the liquid transmitter predates the 10 March success by at least a day. |
| C12-019 | The 10 March entry was attested in Bell's hand as noted on 12 March 1876. | 12 | bell-notebook-1875-1876 | n | Agent read it on notebook p. 45. Two further sets of initials appear in other hands and are NOT identified. |
| C07-001 | The Coinage Act of 1873 is chapter 131 of the third session of the Forty-Second Congress, titled "An Act revising and amending the Laws relative to the Mints, Assay-offices, and Coinage of the United States", and is dated 12 February 1873. | 07 | us-statutes-at-large-v17 | n | Agent read the heading and marginal date on the page image of printed p. 424 (PDF p. 466). Author check: /primary/1873-coinage-act-ch131.md. |
| C07-002 | Section 15 of the act lists the silver coins of the United States as the trade-dollar, half-dollar, quarter-dollar and dime. The standard silver dollar is not among them. | 07 | us-statutes-at-large-v17 | n | Agent read the full list on printed p. 427. The absence is a reading of the enumeration as printed, not an inference about intent. The mechanism at the centre of chapter 07. |
| C07-003 | Section 15 makes those silver coins legal tender at their nominal value for any amount not exceeding five dollars in any one payment. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 427. |
| C07-004 | Section 17 of the act provides that no coins of gold, silver or minor coinage shall thereafter be issued from the mint other than those of the denominations, standards and weights set forth in the act. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 427. Read with section 15 this is the closing clause; what contemporaries understood by it is Q07-3 and is NOT settled by this row. |
| C07-005 | Section 1 of the act establishes the mint of the United States as a bureau of the Treasury Department, headed by a director appointed by the President with the advice and consent of the Senate for a five-year term. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 424. |
| C07-006 | Section 15 fixes the weight of the trade-dollar at four hundred and twenty grains troy. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 427. A figure read from a page image, not from OCR. |
| C07-007 | Section 14 of the act lists the gold coins of the United States and provides that the one-dollar gold piece, at the standard weight of twenty-five and eight-tenths grains, shall be the unit of value. | 07 | us-statutes-at-large-v17 | n | Agent read it on the page image of printed p. 426. The phrase sits in a subordinate clause inside a list of denominations and weights, under the marginal note "Gold coins;". Author check: /primary/1873-coinage-act-ch131-gold-and-repeal.md. |
| C07-008 | Section 14 makes the gold coins a legal tender in all payments, while section 15 limits silver coins to legal tender not exceeding five dollars in any one payment. | 07 | us-statutes-at-large-v17 | n | Agent read both provisions, printed pp. 426 and 427. The asymmetry is in the enacted text, not an inference. |
| C07-009 | Section 13 fixes the standard for both gold and silver coins at nine hundred parts pure metal to one hundred of alloy. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 426. |
| C07-010 | Section 67 provides that the act shall be known as the Coinage act of eighteen hundred and seventy-three, and repeals other acts and parts of acts pertaining to the mints, assay-offices and coinage that are inconsistent with it. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 435. The act names itself; the title is not a later coinage. |
| C07-011 | Sections 15, 17 and 67 together leave no provision under which a standard silver dollar could be struck: the coin is absent from the list of silver coins, no coin outside the list may be issued, and inconsistent prior acts are repealed. | 07 | us-statutes-at-large-v17 | n | Agent read all three sections, printed pp. 427 and 435. This row states how the sections fit, which is a reading of the statute. It asserts nothing about intent, understanding, or consequence - those are Q07-2, Q07-3 and Q07-4 and remain open. |
| C07-012 | Section 66 names the mints at Philadelphia, San Francisco, Carson and Denver, and the assay-offices at New York, Boise City in Idaho, and Charlotte in North Carolina. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 435. |
| C07-013 | The act's sections are numbered consecutively to sixty-seven, the last of which carries the short title and the repealing clause. | 07 | us-statutes-at-large-v17 | n | Agent read sections 66 and 67 adjacent on printed p. 435, and the act ends there; the volume's index gives its extent as printed pp. 424-435. The count follows from the numbering as printed. |
| C07-014 | The act sets salaries for the superintendents, assayers, melters, refiners, coiners and engravers of the mints by name and amount, and provides that salaries and the wages of permanently engaged workmen be paid in monthly instalments. | 07 | us-statutes-at-large-v17 | n | Agent read it on printed p. 426, in the section preceding section 13. |
| C07-015 | The measure that became the Coinage Act of 1873 was a House bill, H. R. No. 2934, titled as revising and amending the laws relative to the mints, assay offices and coinage of the United States. | 07 | cong-globe-42-3 | n | Agent read it in the Index to Senate Proceedings, index p. cxv, from the page image. Author check: /primary/1873-cong-globe-index-coinage-bill.md. |
| C07-016 | On the Senate side the bill was reported at Congressional Globe p. 203, amendments were reported at 363, it was read at 661, discussed at 668, and passed with amendment at 674. | 07 | cong-globe-42-3 | n | Agent read the index entry, index p. cxv. These are the index's own page references; the pages themselves have NOT been read and nothing about the content of the debate follows from this row. |
| C07-017 | The bill went to conference, noted at Congressional Globe pp. 868 and 871; the conference report appears at 1150, was concurred in by the Senate at 1150 and by the House at 1214, and the bill was enrolled at 1282. | 07 | cong-globe-42-3 | n | Agent read the index entry, index p. cxv. |
