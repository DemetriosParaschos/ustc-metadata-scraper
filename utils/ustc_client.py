from __future__ import annotations

import json
from typing import Any

import requests
from bs4 import BeautifulSoup

from classes.class_book import Book

BASE_URL = "https://www.ustc.ac.uk/editions"
REQUEST_TIMEOUT_SECONDS = 20
REQUEST_HEADERS = {"User-Agent": "ustc-scraper/1.0"}


def fetch_ustc_data(ustc_no: str) -> dict[str, Any]:
    url = f"{BASE_URL}/{ustc_no}"

    response = requests.get(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    app = soup.find(id="app")

    if app is None or not app.has_attr("data-page"):
        raise ValueError(f"Could not find USTC data for {ustc_no}")

    return json.loads(app["data-page"])


def get_book(ustc_no: str) -> Book:
    page_data = fetch_ustc_data(ustc_no)

    try:
        edition = page_data["props"]["edition"]
    except KeyError as error:
        raise KeyError(f"Unexpected USTC response shape for {ustc_no}") from error

    return Book.from_dict(edition)
