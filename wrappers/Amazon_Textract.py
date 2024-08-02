
# Amazon Textract https://docs.aws.amazon.com/code-library/latest/ug/python_3_textract_code_examples.html
name = "Amazon Textract"

def extract(pdf):
    print("Must pay - pricing: $1.50 per 1,000 pages")

def format_result(plumber_pdf):
    output = result()
    output.text = plumber_pdf._____ #TODO insert function here to get text, table data, etc.

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

