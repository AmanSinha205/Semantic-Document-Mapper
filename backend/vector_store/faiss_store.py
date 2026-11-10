import faiss
import numpy as np

from backend.models.chunk import Chunk


class FAISSStore:

    def __init__(self):

        self.index = None
        self.chunks = []

    def build(self, chunks: list[Chunk]):

        embeddings = np.array([chunk.embedding for chunk in chunks],dtype=np.float32)

        faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        self.chunks = chunks

    def search(self,query_embedding: list[float],top_k: int = 3) -> list[Chunk]:

        query = np.array(
            [query_embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(query)

        _, indices = self.index.search(
            query,
            top_k
        )

        return [
            self.chunks[i]
            for i in indices[0]
        ]