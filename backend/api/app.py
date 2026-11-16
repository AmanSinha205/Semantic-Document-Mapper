from fastapi import FastAPI

from backend.api.services import (search,pipeline,store,rag)
from backend.config.settings import TOP_K


app = FastAPI(
    title="Semantic Document Mapper API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Semantic Document Mapper API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/search")
def semantic_search(query: str):

    results = search.search(
        query,
        top_k=TOP_K
    )

    return [
        {
            "file": chunk.filename,
            "page": chunk.page_number,
            "text": chunk.text
        }
        for chunk in results
    ]


@app.post("/index")
def index_documents():

    chunks = pipeline.process_directory(
        "data/raw"
    )

    store.build(chunks)

    store.save(
        "data/index/faiss.index",
        "data/index/chunks.json"
    )

    return {
        "chunks_indexed": len(chunks)
    }

@app.get("/ask")
def ask(query: str):

    answer, chunks = rag.ask(query)

    return {
        "answer": answer,
        "sources": [
            {
                "file": chunk.filename,
                "page": chunk.page_number
            }
            for chunk in chunks
        ]
    }