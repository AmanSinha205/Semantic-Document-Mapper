from backend.ingestion.pdf_reader import PDFReader
from backend.preprocessing.document_cleaner import DocumentCleaner
import json
from dataclasses import asdict
from backend.chunking.text_chunker import TextChunker
from backend.embeddings.embedding_generator import EmbeddingGenerator
from backend.search.semantic_search import SemanticSearch


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

    generator = EmbeddingGenerator()

    for chunk in chunks:
        chunk.embedding = generator.generate(chunk.text)

    search = SemanticSearch(generator)

    results = search.search("Where is the exam centre?",chunks,top_k=3,)

    print("\nSearch Results\n")

    for chunk in results:
        print(f"Page {chunk.page_number}")
        print(chunk.text)
        print()

    with open(
        "data/processed/cleaned_sample_admit_card.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            [asdict(chunk) for chunk in chunks],
            file,
            indent=4,
            ensure_ascii=False
        )

    print(len(chunks[0].embedding))
    print("Document cleaned successfully!")
    print(
        "Pages:",
        cleaned_document.page_count
    )


if __name__ == "__main__":
    main()