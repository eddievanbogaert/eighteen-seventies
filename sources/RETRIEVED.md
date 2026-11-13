# RETRIEVED SOURCES

Provenance for every source obtained digitally. `MANIFEST.md` says what the
book uses; this file says where a particular copy came from, when, and in what
form. A source cannot be marked `acquired: "y"` on the strength of a digital
copy unless it has a row here.

The two files are deliberately separate. `MANIFEST.md` is a bibliography and
most of it was seeded from recall. This is a log of things actually fetched,
and nothing enters it that was not opened and read in a session.

## Why the form matters

A digitised source is not the source. It is a photograph of the source, or a
machine's reading of a photograph of the source, and the difference decides
how much weight a claim can carry.

- **`image`** — page images read as images. The strongest form available
  short of the object itself.
- **`transcription`** — a transcription published by the holding institution.
  Strong, but it is someone else's reading, and the transcriber is part of the
  provenance.
- **`ocr`** — machine-read text. **Numerals, proper names, and anything in a
  table are exactly what OCR gets wrong**, which is exactly what rule 1
  covers. A figure, date, or name read only from OCR is not verified. It needs
  the page image.
- **`born-digital`** — the institution's own structured record, e.g. a
  catalogue field or a database row rather than a scan.

## What a row records

- **source_key** — matches `MANIFEST.md`. A source not in the manifest cannot
  be cited, so it cannot be logged here either.
- **url** — the exact URL opened, deep-linked to the page or image used, not
  the collection's front door.
- **retrieved** — ISO date the fetch happened.
- **form** — one of the four above.
- **holding** — the institution whose copy this is, and the collection or
  shelf reference where the page says one.
- **notes** — what was taken from it, anything illegible, and any rights
  restriction the holding institution states.

A link that has rotted is not a reason to delete a row. Record that it rotted
and when; a dead URL with a date and a holding institution is still enough for
a reader to find the thing.

## Log

| source_key | url | retrieved | form | holding | notes |
| --- | --- | --- | --- | --- | --- |
| butler-erewhon-1901 | https://www.gutenberg.org/cache/epub/1906/pg1906.txt | 2026-11-13 | transcription | Project Gutenberg (eBook #1906) | Full text of Erewhon for Q04 transcription. sha256 `9b034d0990931fa4…` cached at `sources/cache/butler-erewhon/9b034d0990931fa4.txt`. |
| bell-patent-174465 | https://patentimages.storage.googleapis.com/10/ab/a3/b4f5c6e5826640/US174465.pdf | 2026-11-13 | image | US Patent Office (via Google Patents page-image service) | All 6 pages read. Retrieved by the author; this host 503s an honestly-identified script. sha256 `300bb898a4981877…`. |
| bell-notebook-1875-1876 | https://www.loc.gov/resource/magbell.25300201/?sp=22 | 2026-11-13 | image | Library of Congress, Manuscript Division, Bell Family Papers | Notebook pp. 40-41, the 10 March 1876 entry. Retrieved by the author; loc.gov 403s this session. sha256 `f51acaace5c8e52c…`. |
| bell-notebook-1875-1876 | https://www.loc.gov/resource/magbell.25300201/?sp=21 | 2026-11-13 | image | Library of Congress, Manuscript Division, Bell Family Papers | Notebook pp. 38-39, the 8-9 March entries. sha256 `bd69d7e98c42789a…`. |
| bell-notebook-1875-1876 | https://www.loc.gov/resource/magbell.25300201/?sp=23 | 2026-11-13 | image | Library of Congress, Manuscript Division, Bell Family Papers | Notebook pp. 42-43, 10 March experiments 2-7. sha256 `06ad6d74a03a50d8…`. |
| bell-notebook-1875-1876 | https://www.loc.gov/resource/magbell.25300201/?sp=24 | 2026-11-13 | image | Library of Congress, Manuscript Division, Bell Family Papers | Notebook pp. 44-45, close of the entry, attested 12 March. sha256 `154cd6b1cb4ad297…`. |
| us-statutes-at-large-v17 | https://drive.google.com/file/d/1m6XhXGDX_HyioYV7v3-VvHj1kxPS2RZy/view | 2026-11-13 | image | Library of Congress digitisation of the 1965 Dennis & Co. photoreproduction; copy supplied by the author | 1174-page scan, no text layer. PDF page = printed page + 42, verified at 7 points. sha256 `3d78ddee7e01b13d…`. |
| cong-globe-42-3 | https://www.congress.gov/cg/ll/llcg/108/0100/0115r115.jpeg | 2026-11-13 | image | Library of Congress, Century of Lawmaking, via congress.gov | Index to Senate Proceedings p. cxv, carrying the coinage bill entry. sha256 `469bdc0a9eca6101…`. |
| cong-globe-42-3 | https://www.congress.gov/cg/ll/llcg/108/0000/0099r099.jpeg | 2026-11-13 | image | Library of Congress, Century of Lawmaking, via congress.gov | Index p. xcix, supplied by the author and used to derive the URL pattern. sha256 `4ba6070e9be478ed…`. |
| calandro-grant-panic-1873 | https://qjae.mises.org/article/137926-ulysses-s-grant-and-the-panic-of-1873 | 2026-11-13 | born-digital | Quarterly Journal of Austrian Economics (Mises Institute) | Full article HTML read; citation details from the publisher's own metadata. sha256 `4f577a2173fd0ac5…`. |
| us-statutes-at-large-v18 | https://archive.org/cors/sim_united-states-united-states-statutes-at-large_1873-1875_18/sim_united-states-united-states-statutes-at-large_1873-1875_18.pdf | 2026-11-13 | image | Internet Archive | 887-page scan. Specie Resumption Act at printed p. 296 = leaf 328. sha256 `ffcf6e9c3b7f9013…`. |
| us-statutes-at-large-v18 | https://archive.org/cors/sim_united-states-united-states-statutes-at-large_1873-1875_18/sim_united-states-united-states-statutes-at-large_1873-1875_18_djvu.txt | 2026-11-13 | ocr | Internet Archive | OCR text, used ONLY to locate the act. Visibly corrupt on this page. sha256 `1b1a03963b058e85…`. |
| grant-papers | https://drive.google.com/file/d/1h7YDX4AJ_JkqjuSsNOYMcoXIBMCti7ym/view | 2026-11-13 | image | Mississippi State University Scholars Junction; copy supplied by the author | Vol. 25 (1874), 535 pp. Veto message read at printed pp. 73-74 = PDF pp. 103-104. OCR layer unreliable, used only to locate. sha256 `6dfc07c3f5ed1111…`. |
| us-revised-statutes-1874 | https://drive.google.com/file/d/1CcCwWt5KUJRXNiAJ2DgfFvxtFIhnOW-h/view | 2026-11-13 | image | Copy supplied by the author | Statutes at Large Vol. 18 Part 1, the Revised Statutes, 1467 pp. Not yet read. sha256 `7f0fcfe169ae440e…`. |
| cong-globe-42-3 | https://archive.org/cors/sim_united-states-congress-congressional-globe_1873/sim_united-states-congress-congressional-globe_1873.pdf | 2026-11-13 | image | Internet Archive | Debates part 1, printed pp. 2-672, 673 leaves. Mint bill proceedings at printed p. 668 = leaf 668. sha256 `1ce20166042e16ed…`. |
| cong-globe-42-3 | https://archive.org/cors/sim_united-states-congress-congressional-globe_1873_0/sim_united-states-congress-congressional-globe_1873_0_djvu.txt | 2026-11-13 | ocr | Internet Archive | Debates part 2 OCR, printed pp. 673-1632. Used ONLY to locate passages. sha256 `9373b920525b76c4…`. |
| butler-erewhon | https://archive.org/cors/erewhonoroverra00butl/erewhonoroverra00butl_djvu.txt | 2026-11-13 | ocr | Internet Archive (London: Trubner & Co., 1872) | First-edition text, 268 leaves. OCR used for counting and collation, NOT for quotation. sha256 `fa60789ed3116c8c…`. |
