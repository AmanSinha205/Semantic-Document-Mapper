from dataclasses import dataclass


@dataclass
class Chunk:
    chunk_id: int
    filename: str
    page_number: int
    text: str
    embedding: list[float] | None = None