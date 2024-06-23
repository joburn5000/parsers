from pypdf import PdfReader
import pdfplumber
import PyPDF2
import camelot

#todo: implement camelot test
tables = camelot.read_pdf('../dataset/Arxiv_papers/3.pdf')
tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
tables[0].parsing_report
# notes: ease of setup lower due to dependency on ghostscript, especially difficult on windows

# todo implement tabula_py test

# reader = PdfReader("../dataset/Arxiv_papers/3.pdf")
# number_of_pages = len(reader.pages)
# for i in range(number_of_pages):   
#     page = reader.pages[i]
#     text = page.extract_text()
#     print(text)

# documentation https://pypdf.readthedocs.io/en/stable/

# with pdfplumber.open("../dataset/Arxiv_papers/3.pdf") as pdf:
#     for page in pdf.pages:
#         print(page.extract_tables(table_settings={}))

# pdfplumber github repo: https://github.com/jsvine/pdfplumber?tab=readme-ov-file#extracting-text
    