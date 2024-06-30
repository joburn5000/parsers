from pypdf import PdfReader
import pdfplumber
import PyPDF2
import camelot

# todo: test PyPDF2, PDFMiner
# Pypdf2 https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader as PdfReader2

reader = PdfReader2("dataset/Arxiv_papers/3.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

# # implement camelot test
# tables = camelot.read_pdf('dataset/Arxiv_papers/3.pdf')
# tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
# tables[0].parsing_report
# notes: ease of setup lower due to dependency on ghostscript, especially difficult on windows

# # todo implement tabula_py test https://github.com/chezou/tabula-py 
# import tabula

# # Read pdf into list of DataFrame
# dfs = tabula.read_pdf("dataset/Arxiv_papers/3.pdf", pages='all')

# # convert PDF into CSV file
# tabula.convert_into("dataset/Arxiv_papers/3.pdf", "output.csv", output_format="csv", pages='all')
# # TODO add notes to evaluation
# # notes: extracts TABLE data to a CSV format. dependency (not necessary to run it though) jpype 'pip install jpype1'

# reader = PdfReader("dataset/Arxiv_papers/3.pdf")
# number_of_pages = len(reader.pages)
# for i in range(number_of_pages):   
#     page = reader.pages[i]
#     text = page.extract_text()
#     print(text)

# documentation https://pypdf.readthedocs.io/en/stable/

# with pdfplumber.open("dataset/Arxiv_papers/3.pdf") as pdf:
#     for page in pdf.pages:
#         print(page.extract_tables(table_settings={}))

# pdfplumber github repo: https://github.com/jsvine/pdfplumber?tab=readme-ov-file#extracting-text
    