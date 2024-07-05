from pypdf import PdfReader
import pdfplumber
import PyPDF2
import camelot

# todo: test Amazon_Textract, Microsoft_Table_Transformer
# todo: summarize findings
# todo: write a post
# todo: put best candidates into the pipeline

# # test llama2parser
# import nest_asyncio
# nest_asyncio.apply()
# from llama_parse import LlamaParse
# parser = LlamaParse(
#     api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
#     result_type="markdown",  # "markdown" and "text" are available
#     num_workers=4,  # if multiple files passed, split in `num_workers` API calls
#     verbose=True,
#     language="en",  # Optionally you can define a language, default=en
# )
# documents = parser.load_data("dataset/Arxiv_papers/3.pdf")
# print(documents)
# # notes: must obtain an API key from llama API
# # Pricing
# # Pricing is based on the number of parameters of the model:
# # <7b = $ 0.0004 / 1K Tokens
# # between 7b and 34b = $ 0.0016 / 1K Tokens
# # >34b = $ 0.0032 / 1K Tokens
# # E.g.:
# # Llama 2 7B: $ 0.0004 / 1K Tokens
# # Llama 2 13B: $ 0.0016 / 1K Tokens
# # Llama 2 70B: $ 0.0032 / 1K Tokens

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


# # test pdf2tables https://github.com/chen1tian/pdf2tables
# # notes: not a good candidate. lacks functionality, last update 5 years ago, it is simply a wrapper for camelot and pdfplumber

# from pdf2tables import pdf_tables

# imgOcrSettings = {
#         'pytesseract_kernel': np.ones((4, 4), np.uint8),
#         'pytesseract_bin_threshold': 127,
#         'pytesseract_iterations': 1,
#         # 单元格面积范围，决定哪些单元格会被选中
#         'pytesseract_areaRange': [10000, 100000],
#         'pytesseract_isDebug': False,
#         # 单元格边框，用来更精确地获取文本
#         'pytesseract_border': 10,
#         'img_ocr_type': ImgOcrType.Pytesseract,
#         'aliyun_appcode': 'b8f41a5f9b664a45af2bc9f58666a17e'
#     }

# tables = extract(
#     'C:/pdf2tables/test_data/Jan-2010.pdf', lang='eng+tha', **imgOcrSettings)
