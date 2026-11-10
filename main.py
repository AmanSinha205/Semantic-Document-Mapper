import json
from dataclasses import asdict

from backend.pipeline.document_pipeline import DocumentPipeline
from backend.search.semantic_search import SemanticSearch
from backend.vector_store.faiss_store import FAISSStore


def main():

    pipeline = DocumentPipeline()

    chunks = pipeline.process(
        "data/raw/sample_admit_card.pdf"
    )    

    store = FAISSStore()

    store.build(chunks)

    print(f"Chunks created: {len(chunks)}")

    search = SemanticSearch(pipeline.generator,store)

    results = search.search("What is the exam date?",top_k=3)

    print("\nSearch Results\n")

    for chunk in results:
        print(f"Chunk {chunk.chunk_id}")
        print(f"Page {chunk.page_number}")
        print(chunk.text)
        print()

    with open(
        "data/processed/chunks.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            [asdict(chunk) for chunk in chunks],
            file,
            indent=4,
            ensure_ascii=False
        )


if __name__ == "__main__":
    main()