from backend.pipeline.document_pipeline import DocumentPipeline
from backend.vector_store.faiss_store import FAISSStore
from backend.search.semantic_search import SemanticSearch


pipeline = DocumentPipeline()

chunks = pipeline.process_directory("data/raw")

store = FAISSStore()
store.build(chunks)

search = SemanticSearch(
    pipeline.generator,
    store
)