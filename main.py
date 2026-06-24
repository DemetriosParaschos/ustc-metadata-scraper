from __future__ import annotations

import argparse
import time
from pathlib import Path

from tqdm import tqdm

from classes.class_book import Book
from utils.csv_utils import load_ustc_numbers
from utils.extract_ustc_nos import extract_ustc_nos
from utils.ustc_client import get_book
from utils.xlsx_export import save_books_to_xlsx


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_MARKDOWN_INPUT = BASE_DIR / "sources" / "ustc_nos.md"
DEFAULT_NUMBERS_OUTPUT = BASE_DIR / "sources" / "ustc_numbers.csv"
DEFAULT_XLSX_OUTPUT = BASE_DIR / "sources" / "ustc_metadata.xlsx"
DEFAULT_DELAY_SECONDS = 0.5


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scrape USTC edition metadata and export the results to Excel."
    )
    parser.add_argument(
        "--input-markdown",
        type=Path,
        default=DEFAULT_MARKDOWN_INPUT,
        help="Markdown file containing USTC numbers.",
    )
    parser.add_argument(
        "--numbers-csv",
        type=Path,
        default=DEFAULT_NUMBERS_OUTPUT,
        help="CSV file created from the markdown input.",
    )
    parser.add_argument(
        "--output-xlsx",
        type=Path,
        default=DEFAULT_XLSX_OUTPUT,
        help="Excel file where the scraped metadata will be stored.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_SECONDS,
        help="Delay in seconds between requests.",
    )
    return parser.parse_args()


def format_path(path: Path) -> str:
    resolved_path = path.resolve()

    try:
        return str(resolved_path.relative_to(BASE_DIR))
    except ValueError:
        return str(resolved_path)


def fetch_books(ustc_numbers: list[str], delay_seconds: float) -> tuple[list[Book], list[str]]:
    books: list[Book] = []
    failed_numbers: list[str] = []

    for ustc_no in tqdm(ustc_numbers, desc="Fetching USTC metadata"):
        try:
            books.append(get_book(ustc_no))
        except Exception as error:
            failed_numbers.append(ustc_no)
            tqdm.write(f"Failed to fetch {ustc_no}: {error}")
        finally:
            if delay_seconds > 0:
                time.sleep(delay_seconds)

    return books, failed_numbers


def main() -> None:
    args = parse_args()

    if args.delay < 0:
        raise SystemExit("--delay must be greater than or equal to 0.")

    csv_file = extract_ustc_nos(args.input_markdown, args.numbers_csv)
    ustc_numbers = load_ustc_numbers(csv_file)

    if not ustc_numbers:
        raise SystemExit(f"No USTC numbers found in {format_path(args.input_markdown)}.")

    books, failed_numbers = fetch_books(ustc_numbers, args.delay)

    if not books:
        raise SystemExit("No records were fetched successfully; not writing an empty workbook.")

    save_books_to_xlsx(books, args.output_xlsx)

    print(f"Saved {len(books)} records to {format_path(args.output_xlsx)}")

    if failed_numbers:
        print(f"Skipped {len(failed_numbers)} records: {', '.join(failed_numbers)}")


if __name__ == "__main__":
    main()
