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
    return tables

def format_result(pdf):
    output = result()
    output.text = pdf._____ #TODO insert function here to get text, table data, etc.

#evaluate data
def evaluate(extracted_data, pdf):
    #TODO
    # test different metrics    
    evaluation = metrics()
    
    # test speed
    start_time = 0 #TODO mark start time
    extract(pdf)
    finish_time = 1 # TODO mark finish time
    evaluation.speed = finish_time - start_time

    # test resource efficiency
    evaluation.memory_usage = ""
    evaluation.cost = 0

    # test accuracy
    expected = get_text(pdf)
    actual = format_results(extract(pdf))
    evaluation.accuracy = evaluate_similarity(expected, actual) # TODO

    # TODO: evaluate robustness    
    evaluation.variation_robustness = ""

    return(evaluation)
