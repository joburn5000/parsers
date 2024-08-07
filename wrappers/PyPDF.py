# pypdf https://pypdf.readthedocs.io/en/stable/

from pypdf import PdfReader
import os
name = "PyPdf"
# todo test
def extract(pdf):
    reader = PdfReader(pdf)
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