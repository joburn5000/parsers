# TODO:
# test and write metrics for each parser
    # accuracy = ""
    # variation_robustness = ""
# compare parsers
    # pdf_plumber
    # PyPDF2
    # PyPDF
    # pdf_2_tables
    # tabula_py
    # PDFMiner
    # camelot
    # llama_parse
    # Amazon_Textract
    # Microsoft_Table_Transformer
# output results in a comprehensible manner
# TODO:
# update requirements.txt


from utils import *
from wrappers import pdf_plumber, PyPDF2, PyPDF, pdf_2_tables, tabula_py, PDFMiner, camelot, llama_parse, Amazon_Textract, Microsoft_Table_Transformer

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]
test_pdf_parsers = pdf_parsers

data = get_pdfs()
# initialize metrics for each parser
for parser in pdf_parsers:
    parser.metrics = metrics()

results = retrieve_data(test_pdf_parsers)

pdf_plumber.metrics.accuracy = "Accurate, from an eyeball test. TODO: use a comparison tool to compare with a ground truth"

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

# TODO print method creation
# TODO use a python logger - one that can also save to a file
# TODO enable CICD on github (eventually)
output_file = open("evaluations.txt", "w")
for parser in pdf_parsers:
    output_file.write(parser.name + "\n")
    output_file.write("Speed: " + str(parser.metrics.speed) + " PDFs per second\n")
    output_file.write("Memory Usage: " + str(parser.metrics.memory_usage) + " MB\n")
    output_file.write("Accuracy: " + parser.metrics.accuracy + "\n")
    output_file.write("Cost: " + parser.metrics.cost + "\n\n")
