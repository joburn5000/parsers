# TODO:
# test and write metrics for each parser
    # accuracy
        # find a similarity comparison tool
    # variation_robustness
        # take notes for different types of PDFs variation
            # see notes for variation in pdfs
# TODO:
# update requirements.txt
# go through remaining TODOs

from utils import *
from wrappers import pdf_plumber, PyPDF2, PyPDF, pdf_2_tables, tabula_py, PDFMiner, camelot, llama_parse, Amazon_Textract, Microsoft_Table_Transformer

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]
test_pdf_parsers = pdf_parsers

data = get_pdfs()

# initialize metrics for each parser
for parser in pdf_parsers:
    parser.metrics = metrics()

results = retrieve_data(test_pdf_parsers)

pdf_plumber.metrics.cost = "Free"
PyPDF2.metrics.cost = "Free"
PyPDF.metrics.cost = "Free"
pdf_2_tables.metrics.cost = "Free"
tabula_py.metrics.cost = "Free"
PDFMiner.metrics.cost = "Free"
camelot.metrics.cost = "Free"
llama_parse.metrics.cost = "Paid"
Amazon_Textract.metrics.cost = "Paid"
Microsoft_Table_Transformer.metrics.cost = "Paid"

output_evaluations(pdf_parsers)
