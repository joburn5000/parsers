from pdfminer.high_level import extract_text
from utils import *
# llama_parse https://github.com/run-llama/llama_parse
import nest_asyncio

def extract(pdf):
    # nest_asyncio.apply()
    # from llama_parse import LlamaParse
    # parser = LlamaParse(
    #     api_key="llx-...",  # can also be set in your env as LLAMA_CLOUD_API_KEY
    #     result_type="markdown",  # "markdown" and "text" are available
    #     num_workers=4,  # if multiple files passed, split in `num_workers` API calls
    #     verbose=True,
    #     language="en",  # Optionally you can define a language, default=en
    # )
    # documents = parser.load_data(pdf)
    print("must obtain an API key from llama API")
    # return documents
    # notes: must obtain an API key from llama API
    # Pricing
    # Pricing is based on the number of parameters of the model:
    # <7b = $ 0.0004 / 1K Tokens
    # between 7b and 34b = $ 0.0016 / 1K Tokens
    # >34b = $ 0.0032 / 1K Tokens
    # E.g.:
    # Llama 2 7B: $ 0.0004 / 1K Tokens
    # Llama 2 13B: $ 0.0016 / 1K Tokens
    # Llama 2 70B: $ 0.0032 / 1K Tokens

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
    evaluation.resource_efficiency = ""
    evaluation.cost = 0

    # test accuracy
    expected = get_text(pdf)
    actual = format_results(extract(pdf))
    evaluation.accuracy = evaluate_similarity(expected, actual) # TODO

    # TODO: evaluate robustness    
    evaluation.variation_robustness = ""

    return(evaluation)
