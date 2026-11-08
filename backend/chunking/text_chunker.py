from backend.models.document import Document
from backend.models.chunk import Chunk


class TextChunker:

    def __init__(self, chunk_size: int = 100, overlap: int = 20):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: Document) -> list[Chunk]:

        chunks = []
        chunk_id = 1

        for page in document.pages:
            words = page.text.split()
            start = 0
            while start < len(words):
                end = start + self.chunk_size
                chunk_text = " ".join(words[start:end])

                if chunk_text:
                    chunks.append(
                        Chunk(
                            chunk_id=chunk_id,
                            page_number=page.page_number,
                            text=chunk_text
                        )
                    )
                    chunk_id += 1
                start += self.chunk_size - self.overlap

        return chunks