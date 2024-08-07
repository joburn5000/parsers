import pdfplumber
import os
name = "Pdf Plumber"

def extract(pdf):
    plumber_pdf = pdfplumber.open(pdf)
    text = ""
    for page in plumber_pdf.pages:
        page_text = page.extract_text()
        text += page_text
        # extract only table data:
        # print(page.extract_tables(table_settings={}))
    return text

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation