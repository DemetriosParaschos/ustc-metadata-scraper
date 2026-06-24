# USTC Scraper

Small Python scraper for pulling edition metadata from the [USTC](https://www.ustc.ac.uk/) website and exporting the results to Excel.

## What it does

1. Reads one or more USTC numbers from `sources/ustc_nos.md`
2. Fetches each edition page from `https://www.ustc.ac.uk/editions/{ustc_no}`
3. Extracts the embedded Inertia JSON payload from `#app[data-page]`
4. Maps the `props.edition` payload to a `Book` dataclass
5. Writes the collected records to `sources/ustc_metadata.xlsx`

## Requirements

- Python 3.11+
- Internet access to the USTC website

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Put your target USTC numbers in `sources/ustc_nos.md`, then run:

```bash
python main.py
```

Optional flags:

```bash
python main.py \
  --input-markdown sources/ustc_nos.md \
  --numbers-csv sources/ustc_numbers.csv \
  --output-xlsx sources/ustc_metadata.xlsx \
  --delay 0.5
```

## Project layout

```text
main.py                  CLI entrypoint
classes/class_book.py    Dataclass for USTC edition records
utils/ustc_client.py     HTTP fetch + JSON extraction
utils/extract_ustc_nos.py
                         Markdown-to-CSV number extraction
utils/csv_utils.py       CSV loading helpers
utils/xlsx_export.py     Excel export
sources/                 Input and generated files
```

## Notes

- The public USTC number is stored in `edition["sn"]`, not `edition["id"]`.
- The scraper preserves the raw edition payload in `Book.raw_data` for troubleshooting.
- `sources/ustc_numbers.csv` and `sources/ustc_metadata.xlsx` are generated outputs and are ignored by Git.
