# pypdf https://pypdf.readthedocs.io/en/stable/

import camelot
import os
name = "camelot"

# todo test
def extract(pdf):
    tables = camelot.read_pdf(pdf)
    return "todo"

def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation