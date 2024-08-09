# TODO:
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
# test tables data
# clean up the individual wrappers
# use instantiations of the parsers, not editing the py object itself
# annotate: write function descriptions, input & output, explanations for each metric

from utils import *
from wrappers import pdf_plumber, PyPDF2, PyPDF, pdf_2_tables, tabula_py, PDFMiner, camelot, llama_parse, Amazon_Textract, Microsoft_Table_Transformer

pdf_parsers = [pdf_plumber, PyPDF, PyPDF2, camelot, Amazon_Textract, Microsoft_Table_Transformer, llama_parse, tabula_py, pdf_2_tables, PDFMiner]
test_pdf_parsers = pdf_parsers

pdfs = get_pdfs()
text_data = retrieve_data(test_pdf_parsers, pdfs)
output_text(text_data)

evaluate_parsers(test_pdf_parsers)
output_evaluations(test_pdf_parsers)
compare_speed(test_pdf_parsers)
compare_memory_usage(test_pdf_parsers)
