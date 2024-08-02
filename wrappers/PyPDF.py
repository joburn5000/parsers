# pypdf https://pypdf.readthedocs.io/en/stable/

from pypdf import PdfReader
import os
name = "PyPdf"
# todo test
def extract(pdf):
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/PyPDF.txt", "w", encoding='utf-8')
    reader = PdfReader(pdf)
    number_of_pages = len(reader.pages)
    for i in range(number_of_pages):   
        page = reader.pages[i]
        output_file.write(page.extract_text())
    return "'reader'"

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
