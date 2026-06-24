from __future__ import annotations

import json
from dataclasses import fields
from pathlib import Path
from typing import Any

from openpyxl import Workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

from classes.class_book import Book


def clean_excel_value(value: Any) -> Any:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)

    if value is None:
        return ""

    if isinstance(value, str):
        return ILLEGAL_CHARACTERS_RE.sub("", value)

    return value


def save_books_to_xlsx(books: list[Book], output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "USTC Metadata"
    sheet.freeze_panes = "A2"

    headers = [
        "USTC No.",
        "Permalink",
        *[
            field.name
            for field in fields(Book)
            if field.name != "raw_data"
        ],
    ]

    sheet.append(headers)

    for book in books:
        row = []

        for header in headers:
            if header == "USTC No.":
                value = book.ustc_no
            elif header == "Permalink":
                value = book.permalink
            else:
                value = getattr(book, header)

            row.append(clean_excel_value(value))

        sheet.append(row)

    sheet.auto_filter.ref = sheet.dimensions
    workbook.save(output_file)
