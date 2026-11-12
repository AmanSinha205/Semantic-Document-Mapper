from backend.ingestion.pdf_reader import PDFReader
from backend.preprocessing.document_cleaner import DocumentCleaner
from backend.chunking.text_chunker import TextChunker
from backend.embeddings.embedding_generator import EmbeddingGenerator
from pathlib import Path


class DocumentPipeline:

    def __init__(self):
        self.reader = PDFReader()
        self.cleaner = DocumentCleaner()
        self.chunker = TextChunker(
            chunk_size=10,
            overlap=2
        )
        self.generator = EmbeddingGenerator()

    def process(self, pdf_path: str):

        document = self.reader.read(pdf_path)

        cleaned_document = self.cleaner.clean(document)

        chunks = self.chunker.chunk(cleaned_document)

        for chunk in chunks:
            chunk.embedding = self.generator.generate(chunk.text)

        return chunks

    def process_directory(self, directory: str):

        all_chunks = []

        directory = Path(directory)

        for pdf in directory.glob("*.pdf"):
            all_chunks.extend(
                self.process(pdf)
            )

        return all_chunks