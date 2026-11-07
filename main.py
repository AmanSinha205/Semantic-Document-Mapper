from backend.ingestion.pdf_reader import PDFReader
import json
from dataclasses import asdict  

def main():
    reader = PDFReader()

    document=reader.read("data/raw/sample_admit_card.pdf")

    with open(
        "data/processed/sample_admit_card.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            asdict(document),
            file,
            indent=4,
            ensure_ascii=False
        )

    print("PDF processed successfully!")
    print("Pages extracted:", document.page_count)

if __name__ == "__main__":
    main()