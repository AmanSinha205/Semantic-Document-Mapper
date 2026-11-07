from backend.ingestion.pdf_reader import PDFReader


def test_pdf_reader():
    reader = PDFReader()

    document = reader.read(
        "data/raw/sample_admit_card.pdf"
    )

    assert document.page_count == 2
    assert len(document.pages) == 2
    assert document.pages[0].text != ""