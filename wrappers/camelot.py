# pypdf https://pypdf.readthedocs.io/en/stable/

import camelot
import os
name = "camelot"

# todo test
def extract(pdf):
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/pdf_plumber.txt", "w", encoding='utf-8')
    tables = camelot.read_pdf(pdf)
    tables.export('foo.csv', f='csv') # json, excel, html, markdown, sqlite
    return "todo"

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation