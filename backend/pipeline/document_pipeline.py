from backend.ingestion.pdf_reader import PDFReader
from backend.preprocessing.document_cleaner import DocumentCleaner
from backend.chunking.text_chunker import TextChunker
from backend.embeddings.embedding_generator import EmbeddingGenerator


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