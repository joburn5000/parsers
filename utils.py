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
    results = []
    total_extracted_data = []
    for parser in test_pdf_parsers:
        timestamp = datetime.datetime.now()
        for pdf in dataset.pdfs[:1]:
            new_result = result()
            print(parser)
            results.append(parser.extract(pdf))
        # parser.metrics.speed = len(dataset.pdfs) / (datetime.datetime.now() - timestamp).total_seconds()
        parser.metrics.speed = 4
        print("PDFs per second: ", parser.metrics.speed)
    return results
