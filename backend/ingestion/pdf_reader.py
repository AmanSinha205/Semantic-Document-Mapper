import warnings
import pymupdf
from pathlib import Path

from backend.models.document import Document
from backend.models.page import Page

class PDFReader:
    """
    Reads PDF documents  and extracts their content
    """

    def __init__(self):
        pass

    def read(self, pdf_path: str | Path) -> Document:
        pdf_path=Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        
        with pymupdf.open(pdf_path) as document:
            metadata = document.metadata
            pages=[]

            for page_index in range(document.page_count):
                page=document.load_page(page_index)
                text= page.get_text().strip()
                
                if not text:
                    warnings.warn(
                        f"No extractable text found on page {page_index + 1}"
                    )                
                pages.append(
                    Page(
                        page_number=page_index + 1,
                        text=text
                    )
                )
            return Document(
                filename=pdf_path.name,
                page_count=document.page_count,
                metadata=metadata,
                pages=pages
            )