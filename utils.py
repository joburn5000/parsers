import os
import datetime

class dataset:
    pdfs = []

class metrics:
    # init TODO
    speed = ""
    resource_efficiency = ""
    cost = ""
    accuracy = ""
    variation_robustness = ""

class result:
    extracted_data = ""
    parser = ""
    pdf = ""
    evaluation = ""

class pdf_parser:
    type = ""
    extract = ""
    metrics = metrics()
    result = result()


# initialize data: get pdfs from dataset folder
def get_pdfs():
    Arxiv_papaers_directory = "dataset/Arxiv_papers"
    public_SEC_docs_directory = "dataset/public_SEC_docs"
    Arxiv_files = os.listdir(Arxiv_papaers_directory)
    public_SEC_pdfs = os.listdir(public_SEC_docs_directory)
    data = dataset()
    for pdf in Arxiv_files:
        data.pdfs.append(Arxiv_papaers_directory+"/"+pdf)
    for pdf in public_SEC_pdfs:
        data.pdfs.append(public_SEC_docs_directory+"/"+pdf)
    return data

def retrieve_data(test_pdf_parsers):
    #retrieve data for each pdf
    num_pdfs = len(dataset.pdfs)
    for parser in test_pdf_parsers:
        timestamp = datetime.datetime.now()
        for pdf in dataset.pdfs:
            parser.extract(pdf)
        seconds_elapsed =  (datetime.datetime.now() - timestamp).total_seconds()
        parser.metrics.speed = "n/a" if seconds_elapsed == 0 else num_pdfs / seconds_elapsed
    return
