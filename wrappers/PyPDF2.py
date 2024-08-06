# PyPDF2 https://pypi.org/project/PyPDF2/
from PyPDF2 import PdfReader as PdfReader2
import os
name = "PyPdf2"

# todo test tabula
def extract(pdf):
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/PyPDF2.txt", "w", encoding='utf-8')
    reader = PdfReader2(pdf)
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        page_text = page.extract_text()
        output_file.write(page_text)
        text += page_text
    return reader

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation