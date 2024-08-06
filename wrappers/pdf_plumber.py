import pdfplumber
import os
name = "Pdf Plumber"

def extract(pdf):
    plumber_pdf = pdfplumber.open(pdf)
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/pdf_plumber.txt", "w", encoding='utf-8')
    text = ""
    for page in plumber_pdf.pages:
        page_text = page.extract_text()
        output_file.write(page_text)
        text += page_text
        # extract only table data:
        # print(page.extract_tables(table_settings={}))
    return text

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation