# write a script to evaluate them correctly. 
# have a dataset class, class for metrics, 4th class: type of PDF parser
# define input & output. 
# put those inputs & outputs. 
# make them defined. 
# go and only change the PDF parser class

import os
from utils import *
from extraction_functions import *

pdf_plumber = pdf_parser()
PyPDF = pdf_parser() #TODO change the names so they're unique from the library
PyPDF2 =  pdf_parser()
camelot = pdf_parser()
Amazon_Textract = pdf_parser()
Microsoft_Table_Transformer = pdf_parser()
llama_parse = pdf_parser()
tabula_py = pdf_parser()
pdf2tables = pdf_parser()
PDFMiner = pdf_parser()

# TODO fill in name for each pdf parser
# TODO extract should return a result class
# TODO move these from the extract function file to the wrapper
pdf_plumber.extract = pdf_plumber_extract
PyPDF2.extract = PyPDF2_extract
camelot.extract = camelot_extract
Amazon_Textract.extract = Amazon_Textract_extract
Microsoft_Table_Transformer.extract = Microsoft_Table_Transformer_extract
llama_parse.extract = llama_parse_extract
tabula_py.extract = tabula_py_extract
pdf2tables.extract = pdf2tables_extract
PyPDF.extract = PyPDF_extract
PDFMiner.extract = PDFMiner_extract

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf2tables, PDFMiner]
test_pdf_parsers = [tabula_py] # PyPDF2, PDFMiner, camelot, llama_parse, pdf2tables, Amazon_Textract, Microsoft_Table_Transformer
dataset = dataset()
metrics = metrics()

# initialize data: get pdfs from dataset folder
Arxiv_papaers_directory = "dataset/Arxiv_papers"
public_SEC_docs_directory = "dataset/public_SEC_docs"
Arxiv_files = os.listdir(Arxiv_papaers_directory)
public_SEC_pdfs = os.listdir(public_SEC_docs_directory)
for pdf in Arxiv_files:
    dataset.pdfs.append(Arxiv_papaers_directory+"/"+pdf)
for pdf in public_SEC_pdfs:
    dataset.pdfs.append(public_SEC_docs_directory+"/"+pdf)
print(dataset.pdfs)
# TODO set up the classes correctly

#retrieve data for each pdf
results = []
total_extracted_data = []
for parser in test_pdf_parsers:
    for pdf in dataset.pdfs:
        new_result = result()
        results.append(parser.extract(pdf))

#evaluate data
def evaluate(extracted_data, pdf):
    #TODO
    evaluation = metrics()
    return(evaluation)

evaluations = []
for extracted_data, pdf in zip(total_extracted_data, dataset.pdfs):
    evaluate(extracted_data, pdf)

# notes for each
pdf_plumber.metrics.speed = "very fast. TODO: number of pages per second"
pdf_plumber.metrics.resource_efficiency = "very efficient: TODO CPU/GPU utilization metrics"
pdf_plumber.metrics.cost = "Free"
pdf_plumber.metrics.accuracy = "Accurate, from an eyeball test. TODO: use a comparison tool to compare with a ground truth"

# TODO print method creation
# TODO use a python logger - one that can also save to a file
# TODO enable CICD on github (eventually)
for evaluation in evaluations:
    print(evaluation)
