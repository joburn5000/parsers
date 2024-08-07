# PyPDF2 https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader as PdfReader2
import os
name = "PyPdf2"

# todo test tabula
def extract(pdf):
    reader = PdfReader2(pdf)
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        page_text = page.extract_text()
        text += page_text
    return text

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation