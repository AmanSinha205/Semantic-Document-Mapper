from backend.chunking.text_chunker import TextChunker
from backend.models.document import Document
from backend.models.page import Page


def test_text_chunker():

    document = Document(
        filename="test.pdf",
        page_count=1,
        metadata={},
        pages=[
            Page(
                page_number=1,
                text="one two three four five six seven eight nine ten"
            )
        ]
    )

    chunker = TextChunker(
        chunk_size=5,
        overlap=2
    )

    chunks = chunker.chunk(document)

    assert len(chunks) > 1
    assert chunks[0].page_number == 1
    assert chunks[0].text != ""