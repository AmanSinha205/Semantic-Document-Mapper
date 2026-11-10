from backend.embeddings.embedding_generator import EmbeddingGenerator
from backend.vector_store.faiss_store import FAISSStore


class SemanticSearch:

    def __init__(
        self,
        generator: EmbeddingGenerator,
        store: FAISSStore
    ):

        self.generator = generator
        self.store = store

    def search(
        self,
        query: str,
        top_k: int = 3
    ):

        embedding = self.generator.generate(query)

        return self.store.search(
            embedding,
            top_k
        )