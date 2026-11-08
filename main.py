from backend.ingestion.pdf_reader import PDFReader
from backend.preprocessing.document_cleaner import DocumentCleaner
import json
from dataclasses import asdict
from backend.chunking.text_chunker import TextChunker


def main():

    reader = PDFReader()

    document = reader.read(
        "data/raw/sample_admit_card.pdf"
    )


    cleaner = DocumentCleaner()

    cleaned_document = cleaner.clean(document)

    chunker = TextChunker(chunk_size=10,overlap=2)

    chunks = chunker.chunk(cleaned_document)

    print(f"Chunks created: {len(chunks)}")

    for chunk in chunks:
        print(f"\nChunk {chunk.chunk_id}")
        print(f"Page: {chunk.page_number}")
        print(chunk.text)

    with open(
        "data/processed/cleaned_sample_admit_card.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            asdict(cleaned_document),
            file,
            indent=4,
            ensure_ascii=False
        )


    print("Document cleaned successfully!")
    print(
        "Pages:",
        cleaned_document.page_count
    )


if __name__ == "__main__":
    main()