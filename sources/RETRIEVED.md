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
| butler-erewhon | https://www.gutenberg.org/cache/epub/1906/pg1906.txt | 2026-11-13 | transcription | Project Gutenberg (eBook #1906) | Full text of Erewhon for Q04 transcription. sha256 `9b034d0990931fa4…` cached at `sources/cache/butler-erewhon/9b034d0990931fa4.txt`. |
