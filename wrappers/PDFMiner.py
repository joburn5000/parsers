from pdfminer.high_level import extract_text
import os
# PDFMiner https://github.com/pdfminer/pdfminer.six
name = "Pdf Miner"

def extract(pdf):
    text = extract_text(pdf)
    return text

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation