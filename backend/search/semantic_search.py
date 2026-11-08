import numpy as np

from backend.models.chunk import Chunk
from backend.embeddings.embedding_generator import EmbeddingGenerator


class SemanticSearch:

    def __init__(self, generator: EmbeddingGenerator):
        self.generator = generator

    def search(
        self,
        query: str,
        chunks: list[Chunk],
        top_k: int = 3,
    ) -> list[Chunk]:

        query_embedding = np.array(
            self.generator.generate(query)
        )

        scores = []

        for chunk in chunks:

            chunk_embedding = np.array(chunk.embedding)

            similarity = (
                np.dot(query_embedding, chunk_embedding)
                / (
                    np.linalg.norm(query_embedding)
                    * np.linalg.norm(chunk_embedding)
                )
            )

            scores.append((similarity, chunk))

        scores.sort(reverse=True, key=lambda x: x[0])

        return [chunk for _, chunk in scores[:top_k]]