import pdfplumber
import os
name = "Pdf Plumber"

def extract(pdf):
    plumber_pdf = pdfplumber.open(pdf)
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/pdf_plumber.txt", "w", encoding='utf-8')
    for page in plumber_pdf.pages:
        output_file.write(page.extract_text())
        # extract only table data:
        # print(page.extract_tables(table_settings={}))
    return plumber_pdf

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation