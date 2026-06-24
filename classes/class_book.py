from dataclasses import dataclass, fields
from typing import Any


@dataclass
class Book:
    id: int | None = None
    status: str = ""
    status_detail: str = ""
    type: str = ""
    sn: str = ""
    heading: str = ""

    author_role_1: str = ""
    author_name_1: str = ""
    author_role_2: str = ""
    author_name_2: str = ""
    author_role_3: str = ""
    author_name_3: str = ""
    author_role_4: str = ""
    author_name_4: str = ""
    author_role_5: str = ""
    author_name_5: str = ""
    author_role_6: str = ""
    author_name_6: str = ""
    author_role_7: str = ""
    author_name_7: str = ""
    author_role_8: str = ""
    author_name_8: str = ""

    std_title: str = ""
    std_imprint: str = ""
    std_colophon: str = ""

    country: str = ""
    region: str = ""
    place: str = ""

    printer_name_1: str = ""
    printer_name_2: str = ""
    printer_name_3: str = ""
    printer_name_4: str = ""

    year: str = ""
    format: str = ""
    pagination: str = ""
    signatures: str = ""

    fingerprint_LOC: str = ""
    fingerprint_STCN: str = ""

    classification_1: str = ""
    classification_2: str = ""
    classification_3: str = ""
    classification_4: str = ""

    language_1: str = ""
    language_2: str = ""
    language_3: str = ""
    language_4: str = ""

    female_author: int = 0
    female_printer: int = 0

    created_by: str = ""
    updated_by: str = ""
    created_at: str | None = None
    updated_at: str | None = None

    raw_data: dict[str, Any] | None = None

    @property
    def ustc_no(self) -> str:
        return self.sn or str(self.id or "")

    @property
    def permalink(self) -> str:
        return f"https://www.ustc.ac.uk/editions/{self.ustc_no}"

    @property
    def title(self) -> str:
        return self.std_title

    @property
    def author(self) -> str:
        return self.author_name_1

    @property
    def imprint(self) -> str:
        return self.std_imprint

    @property
    def publication_year(self) -> str:
        return self.year

    @property
    def printer(self) -> str:
        return self.printer_name_1

    @property
    def language(self) -> str:
        return self.language_1

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Book":
        field_names = {field.name for field in fields(cls)}

        book_data = {
            key: value
            for key, value in data.items()
            if key in field_names and key != "raw_data"
        }

        return cls(**book_data, raw_data=data)
