from dataclasses import dataclass
from typing import Any

from backend.models.page import Page


@dataclass
class Document:
    filename: str
    page_count: int
    metadata: dict[str, Any]
    pages: list[Page]