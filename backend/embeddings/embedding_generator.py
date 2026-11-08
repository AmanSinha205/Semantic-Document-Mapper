from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate(self, text: str) -> list[float]:
        return self.model.encode(text,convert_to_numpy=True).tolist()