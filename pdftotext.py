from pypdf import PdfReader
import pdfplumber

# pypdf PdfReader
# reader = PdfReader("example.pdf")
# number_of_pages = len(reader.pages)
# for i in range(number_of_pages):   
#     page = reader.pages[i]
#     text = page.extract_text()
#     print(text)

# documentation https://pypdf.readthedocs.io/en/stable/


with pdfplumber.open("example.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_tables(table_settings={}))

# pdfplumber github repo: https://github.com/jsvine/pdfplumber?tab=readme-ov-file#extracting-text
    