class LLMService:

    def generate_answer(self,query: str,context: list[str]) -> str:

        prompt = f"""
        Question:
        {query}

        Context:
        {'-'*40}
        {chr(10).join(context)}
        {'-'*40}
        """

        return prompt