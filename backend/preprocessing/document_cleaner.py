from backend.models.document import Document
from backend.models.page import Page
from backend.preprocessing.text_cleaner import TextCleaner


class DocumentCleaner:

    def __init__(self):
        self.text_cleaner = TextCleaner()


    def clean(self, document: Document) -> Document:

        cleaned_pages = []

        for page in document.pages:

            cleaned_text = self.text_cleaner.clean(
                page.text
            )

            cleaned_pages.append(
                Page(
                    page_number=page.page_number,
                    text=cleaned_text
                )
            )

        return Document(
            filename=document.filename,
            page_count=document.page_count,
            metadata=document.metadata,
            pages=cleaned_pages
        )