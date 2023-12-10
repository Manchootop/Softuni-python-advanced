import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file_path):
    text = ""

    with fitz.open(pdf_file_path) as pdf_document:
        num_pages = pdf_document.page_count

        for page_number in range(num_pages):
            page = pdf_document[page_number]
            text += page.get_text()

    return text

if __name__ == "__main__":
    pdf_file_path = "05.Test-Levels-and-Test-Types.pdf"  # Replace with your file path
    extracted_text = extract_text_from_pdf(pdf_file_path)

    with open("output.txt", "a", encoding="utf-8") as output_file:
        output_file.write(extracted_text)

    print("Text extracted and saved to 'output.txt'")
