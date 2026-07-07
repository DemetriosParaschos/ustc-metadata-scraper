# USTC Metadata Scraper

[![DOI: 10.5281/zenodo.21242822](https://zenodo.org/badge/DOI/10.5281/zenodo.21242822.svg)](https://doi.org/10.5281/zenodo.21242822)

Python software for the automated acquisition, extraction, and structuring of bibliographic metadata from the Universal Short Title Catalogue (USTC).

Developed as part of doctoral research to support the construction of an original research database of early printed books.

---

## Research context

This software was developed within the ERC Starting Grant project **VERITRACE** ("Traces de la Vérité"), led by Prof. Dr. Cornelis J. Schilt, as part of the author's doctoral research. It automates the acquisition, validation, and structuring of bibliographic metadata from the Universal Short Title Catalogue (USTC), forming an integral component of the project's digital research infrastructure.

The software was created to support the construction of an original research database that underpins the author's PhD dissertation. By replacing the manual transcription of bibliographic metadata with an automated and reproducible workflow, it substantially reduces the time required for data collection while improving consistency, reliability, and data quality. The resulting standardized datasets provide a transparent foundation for quantitative, bibliographic, and computational analyses within both the dissertation and the broader objectives of the VERITRACE project.

---

## Features

- Automated retrieval of edition metadata from the USTC website
- Extraction of structured metadata from embedded JSON
- Mapping of metadata into strongly typed Python objects
- Export of datasets to Microsoft Excel
- Modular architecture for extension and reuse
- Reproducible workflow for research data acquisition

---

## Workflow

1. Reads one or more USTC numbers from `sources/ustc_nos.md`
2. Retrieves the corresponding edition pages
3. Extracts the embedded Inertia JSON payload
4. Converts metadata into a `Book` dataclass
5. Exports the resulting dataset to Excel

---

## Requirements

- Python 3.11+
- Internet access to the USTC website

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

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

---

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

---

## Notes

- The public USTC number is stored in `edition["sn"]`, not `edition["id"]`.
- The scraper preserves the raw edition payload in `Book.raw_data` for troubleshooting.
- `sources/ustc_numbers.csv` and `sources/ustc_metadata.xlsx` are generated outputs and are ignored by Git.

---

## Citation

If this software contributes to your research, please cite it as:

Paraschos, D. (2026). *USTC Metadata Scraper* (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21242822


For more information, vid. `CITATION.cff`.


---

## License

This software is released under **The Unlicense**.

The rationale behind this licensing choice and the author's commitment to open scientific research are described in `OPEN_SCIENCE.md`.