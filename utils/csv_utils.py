import csv
from pathlib import Path


def load_ustc_numbers(csv_file: Path) -> list[str]:
    numbers: list[str] = []
    seen: set[str] = set()

    with csv_file.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            number = row.get("USTC No.")
            if not number:
                continue

            cleaned_number = number.strip()
            if cleaned_number and cleaned_number not in seen:
                seen.add(cleaned_number)
                numbers.append(cleaned_number)

    return numbers
