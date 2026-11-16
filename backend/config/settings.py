from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv()


BASE_DIR = Path.cwd()

RAW_DATA_DIR = BASE_DIR / "data" / "raw"

INDEX_DIR = BASE_DIR / "data" / "index"

FAISS_INDEX_PATH = INDEX_DIR / "faiss.index"

CHUNK_METADATA_PATH = INDEX_DIR / "chunks.json"

CHUNK_SIZE = 10

CHUNK_OVERLAP = 2

TOP_K = 3

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")