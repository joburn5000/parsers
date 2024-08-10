# pypdf https://pypdf.readthedocs.io/en/stable/

import camelot
import os
name = "camelot"

# todo test
def extract(pdf):
    tables = camelot.read_pdf(pdf)
    return "todo"

def evaluate():
    evaluation = {"Cost": 0, "Accuracy": 0}         
    return evaluation