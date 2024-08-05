# TODO:
# fix bug: pdf_plumber is not getting through all the pdfs
# add evaluation notes to the python object themselves
# test and write metrics for each parser
    # accuracy
        # how to measure F1 score: LLM model, retrieval model? (select one, define retrieval)
        # create some ground truth data
        # find a similarity comparison tool
    # variation_robustness
        # take notes for different types of PDFs variation
            # see notes for variation in pdfs
            # identify types of tables: table in row, column, 
                # variation of size, color scheme, highlighted rows, 
                # script size & font size. See how well they do on 
                # different tables. Find automation for tables, then 
                # do it for images. understand where images stand.
# calculate average data for metric results across all pdf parsers
# test tables data
# clean up the individual wrappers
# use instantiations of the parsers, not editing the py object itself
# annotate: write function descriptions, input & output, explanations for each metric

from utils import *
from wrappers import pdf_plumber, PyPDF2, PyPDF, pdf_2_tables, tabula_py, PDFMiner, camelot, llama_parse, Amazon_Textract, Microsoft_Table_Transformer

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]
test_pdf_parsers = pdf_parsers

pdfs = get_pdfs()
results = retrieve_data(test_pdf_parsers, pdfs)

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
