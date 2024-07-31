# tabula_py https://github.com/chezou/tabula-py 
import tabula
name = "Tabula Py"

# todo test tabula
def extract(pdf):
    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf("dataset/Arxiv_papers/3.pdf", pages='all')
    # convert PDF into CSV file
    tabula.convert_into("dataset/Arxiv_papers/3.pdf", "tabula_output.csv", output_format="csv", pages='all')
    # notes: extracts TABLE data to a CSV format. dependency (not necessary to run it though) jpype 'pip install jpype1'
    return dfs

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
    evaluation.resource_efficiency = ""
    evaluation.cost = 0

    # test accuracy
    expected = get_text(pdf)
    actual = format_results(extract(pdf))
    evaluation.accuracy = evaluate_similarity(expected, actual) # TODO

    # TODO: evaluate robustness    
    evaluation.variation_robustness = ""

    return(evaluation)
