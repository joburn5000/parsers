# pypdf https://pypdf.readthedocs.io/en/stable/

from pypdf import PdfReader
import os
name = "PyPdf"
# todo test
def extract(pdf):
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/PyPDF.txt", "w", encoding='utf-8')
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    for i in range(number_of_pages):   
        page = reader.pages[i]
        output_file.write(page.extract_text())
    return "'reader'"

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation