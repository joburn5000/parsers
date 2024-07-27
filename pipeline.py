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

import os
import datetime #TODO add to requirements.txt
from utils import *
from wrappers import pdf_plumber, PyPDF2, PyPDF, pdf_2_tables, tabula_py, PDFMiner, camelot, llama_parse, Amazon_Textract, Microsoft_Table_Transformer

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]
test_pdf_parsers = [pdf_plumber]

# initialize data: get pdfs from dataset folder
Arxiv_papaers_directory = "dataset/Arxiv_papers"
public_SEC_docs_directory = "dataset/public_SEC_docs"
Arxiv_files = os.listdir(Arxiv_papaers_directory)
public_SEC_pdfs = os.listdir(public_SEC_docs_directory)
dataset = dataset()
for pdf in Arxiv_files:
    dataset.pdfs.append(Arxiv_papaers_directory+"/"+pdf)
for pdf in public_SEC_pdfs:
    dataset.pdfs.append(public_SEC_docs_directory+"/"+pdf)

# initialize metrics for each parser
for parser in pdf_parsers:
    parser.metrics = metrics()

#retrieve data for each pdf
results = []
total_extracted_data = []
for parser in test_pdf_parsers:
    timestamp = datetime.datetime.now()
    for pdf in dataset.pdfs:
        new_result = result()
        print(parser)
        results.append(parser.extract(pdf))
    parser.metrics.speed = len(dataset.pdfs) / (datetime.datetime.now() - timestamp).total_seconds()
    print("PDFs per second: ", parser.metrics.speed)

#evaluate data
def evaluate(extracted_data, pdf):
    #TODO
    evaluation = metrics()
    return(evaluation)

evaluations = []
for extracted_data, pdf in zip(total_extracted_data, dataset.pdfs):
    evaluate(extracted_data, pdf)

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

pdf_plumber.metrics.speed
PyPDF2.metrics.speed
PyPDF.metrics.speed
pdf_2_tables.metrics.speed
tabula_py.metrics.speed
PDFMiner.metrics.speed
camelot.metrics.speed
llama_parse.metrics.speed
Amazon_Textract.metrics.speed
Microsoft_Table_Transformer.metrics.speed

# TODO print method creation
# TODO use a python logger - one that can also save to a file
# TODO enable CICD on github (eventually)
for evaluation in evaluations:
    print(evaluation)
