import pdfplumber
from pypdf import PdfReader
# todo put each pdf_parser into its own class

def pdf_plumber_extract(pdf):
    with pdfplumber.open(pdf) as plumber_pdf:
        for page in plumber_pdf.pages:
            print(page.extract_text())
            # extract only table data:
            # print(page.extract_tables(table_settings={}))
    return

def PyPDF2_extract():
    return
    
def camelot_extract():
    return
    
def Amazon_Textract_extract():
    return
    
def Microsoft_Table_Transformer_extract():
    return
    
def llama2parser_extract():
    return
    
def tabula_py_extract():
    return
    
def pdf2tables_extract():
    return
    
def pdfreader_extract(pdf):
    reader = PdfReader("dataset/Arxiv_papers/3.pdf")
    number_of_pages = len(reader.pages)
    for i in range(number_of_pages):   
        page = reader.pages[i]
        text = page.extract_text()
        print(text)
    return
    
def PDFMiner_extract():
    return
    