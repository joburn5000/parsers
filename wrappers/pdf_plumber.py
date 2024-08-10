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
    evaluation = {"Cost": 0, "Accuracy": 0.8}
    # Accuracy notes:
        # 3.pdf
            # A couple smashed text "Fortheuntrustedcentralserversetting,weprovablyshowthatfederatedlearningis..."
            # 

    return evaluation