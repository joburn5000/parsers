from pypdf import PdfReader
import pdfplumber
import PyPDF2
import camelot
# todo test pdf2tables

# todo test llama2parser
import nest_asyncio
nest_asyncio.apply()
from llama_parse import LlamaParse
parser = LlamaParse(
    api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown",  # "markdown" and "text" are available
    num_workers=4,  # if multiple files passed, split in `num_workers` API calls
    verbose=True,
    language="en",  # Optionally you can define a language, default=en
)
documents = parser.load_data("dataset/Arxiv_papers/3.pdf")
print(documents)

# # test PyPDF2
# # Pypdf2 https://pypi.org/project/PyPDF2/
# # todo: can it do tables?
# from PyPDF2 import PdfReader as PdfReader2

# reader = PdfReader2("dataset/Arxiv_papers/3.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text)

# # test PDFMiner (community maintained: https://github.com/pdfminer/pdfminer.six) (this one is command-line only: https://pypi.org/project/pdfminer/)
# from pdfminer.high_level import extract_text
# text = extract_text("dataset/Arxiv_papers/3.pdf")
# print(text)
# # notes: very sloppy extraction result (lots of extra whitespace)

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
    