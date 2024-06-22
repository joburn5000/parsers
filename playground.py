from pypdf import PdfReader
import pdfplumber
import PyPDF2

#todo: implement camelot test
import camelot
# tables = camelot.read_pdf('foo.pdf')
# tables
# <TableList n=1>
# tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
# tables[0]
# <Table shape=(7, 7)>
# tables[0].parsing_report

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
    