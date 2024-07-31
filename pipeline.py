# TODO:
# test and write metrics for each parser
    # cost = ""
    # speed = ""
    # resource_efficiency = ""
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
# make an init.py that handles data initialization


from utils import *
from wrappers import pdf_plumber, PyPDF2, PyPDF, pdf_2_tables, tabula_py, PDFMiner, camelot, llama_parse, Amazon_Textract, Microsoft_Table_Transformer

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]
test_pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]

data = get_pdfs()
# initialize metrics for each parser
for parser in pdf_parsers:
    parser.metrics = metrics()

results = retrieve_data(test_pdf_parsers)

pdf_plumber.metrics.speed = "very fast. TODO: number of pages per second"
pdf_plumber.metrics.resource_efficiency = "very efficient: TODO CPU/GPU utilization metrics"
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
    output_file.write("Speed: " + parser.metrics.speed + "\n")
    output_file.write("Resource Efficiency: " + parser.metrics.resource_efficiency + "\n")
    output_file.write("Accuracy: " + parser.metrics.accuracy + "\n")
    output_file.write("Cost " + parser.metrics.cost + "\n\n")
