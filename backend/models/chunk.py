from dataclasses import dataclass


@dataclass
class Chunk:
    chunk_id: int
    page_number: int
    text: str
    embedding: list[float] | None = None