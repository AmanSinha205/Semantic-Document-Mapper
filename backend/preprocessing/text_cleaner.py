import re

class TextCleaner:
    """
    Cleans extracted document text.
    """

    def clean(self, text: str) -> str:
        """
        Perform basic text cleaning.
        """

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text