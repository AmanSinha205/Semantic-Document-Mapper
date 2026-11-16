from sentence_transformers import SentenceTransformer
from backend.config.settings import EMBEDDING_MODEL


class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def generate(self, text: str) -> list[float]:
        return self.model.encode(text,convert_to_numpy=True).tolist()