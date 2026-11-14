from backend.pipeline.document_pipeline import DocumentPipeline
from backend.vector_store.faiss_store import FAISSStore
from backend.search.semantic_search import SemanticSearch
from pathlib import Path


pipeline = DocumentPipeline()
store = FAISSStore()

index_path = Path("data/index/faiss.index")
metadata_path = Path("data/index/chunks.json")

if index_path.exists() and metadata_path.exists():

    print("Loading existing FAISS index...")

    store.load(
        str(index_path),
        str(metadata_path)
    )

else:

    print("Building new FAISS index...")

    chunks = pipeline.process_directory(
        "data/raw"
    )

    store.build(chunks)

    store.save(
        str(index_path),
        str(metadata_path)
    )

search = SemanticSearch(
    pipeline.generator,
    store
)