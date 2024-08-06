from pdfminer.high_level import extract_text
import os
# PDFMiner https://github.com/pdfminer/pdfminer.six
name = "Pdf Miner"

def extract(pdf):
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/PDFMiner.txt", "w", encoding='utf-8')
    text = extract_text(pdf)
    output_file.write(text)
    return text

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation