from __future__ import annotations

import csv
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_INPUT_FILE = BASE_DIR / "sources" / "ustc_nos.md"
DEFAULT_OUTPUT_FILE = BASE_DIR / "sources" / "ustc_numbers.csv"
USTC_NUMBER_PATTERN = re.compile(r"USTC No\.\s*(\d+)")


def extract_ustc_nos(
    input_file: Path = DEFAULT_INPUT_FILE,
    output_file: Path = DEFAULT_OUTPUT_FILE,
) -> Path:
    text = input_file.read_text(encoding="utf-8")
    ustc_numbers = USTC_NUMBER_PATTERN.findall(text)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USTC No."])
        for number in ustc_numbers:
            writer.writerow([number])

    print(f"Extracted {len(ustc_numbers)} USTC numbers to {output_file}")

    return output_file
