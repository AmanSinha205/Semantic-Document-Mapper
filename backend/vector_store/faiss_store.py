import json
from dataclasses import asdict
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

    def save(self, index_path: str, metadata_path: str):

        faiss.write_index(
            self.index,
            index_path
        )

        with open(
            metadata_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                [asdict(chunk) for chunk in self.chunks],
                f,
                indent=4,
                ensure_ascii=False
            )

    def load(self,index_path: str,metadata_path: str):

        self.index = faiss.read_index(index_path)

        with open( metadata_path,"r",encoding="utf-8") as f:
            data = json.load(f)

        self.chunks = [Chunk(**chunk) for chunk in data ]