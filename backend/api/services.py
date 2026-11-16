from backend.pipeline.document_pipeline import DocumentPipeline
from backend.vector_store.faiss_store import FAISSStore
from backend.search.semantic_search import SemanticSearch
from pathlib import Path
from backend.llm.llm_service import LLMService
from backend.rag.rag_service import RAGService
from backend.config.settings import (RAW_DATA_DIR,FAISS_INDEX_PATH,CHUNK_METADATA_PATH)


pipeline = DocumentPipeline()
store = FAISSStore()

index_path = Path(str(FAISS_INDEX_PATH))
metadata_path = Path(str(CHUNK_METADATA_PATH))

if index_path.exists() and metadata_path.exists():

    print("Loading existing FAISS index...")

    store.load(
        str(index_path),
        str(metadata_path)
    )

else:

    print("Building new FAISS index...")

    chunks = pipeline.process_directory(str(RAW_DATA_DIR))

    store.build(chunks)

    store.save(
        str(index_path),
        str(metadata_path)
    )

search = SemanticSearch(pipeline.generator,store)
llm = LLMService()

rag = RAGService(search,llm)