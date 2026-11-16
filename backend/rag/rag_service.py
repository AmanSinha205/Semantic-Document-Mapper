from backend.search.semantic_search import SemanticSearch
from backend.llm.llm_service import LLMService


class RAGService:

    def __init__(self,search: SemanticSearch,llm: LLMService):
        self.search = search
        self.llm = llm

    def ask(self, query: str):

        chunks = self.search.search(query,top_k=3)

        context = [chunk.text  for chunk in chunks  ]

        answer = self.llm.generate_answer(query,context)

        return answer, chunks