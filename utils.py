import os
import datetime
import tracemalloc


class dataset:
    pdfs = []

class metrics:
    # init TODO
    speed = ""
    memory_usage = ""
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
    data = dataset()
    Arxiv_papaers_directory = "dataset/Arxiv_papers"
    Arxiv_files = os.listdir(Arxiv_papaers_directory)
    for pdf in Arxiv_files:
        data.pdfs.append(Arxiv_papaers_directory+"/"+pdf)
    public_SEC_docs_directory = "dataset/public_SEC_docs"
    public_SEC_pdfs = os.listdir(public_SEC_docs_directory)
    for pdf in public_SEC_pdfs:
        data.pdfs.append(public_SEC_docs_directory+"/"+pdf)
    return data

def retrieve_data(test_pdf_parsers):
    #retrieve data for each pdf
    
    num_pdfs = len(dataset.pdfs)
    for parser in test_pdf_parsers:
        # track memory usage
        tracemalloc.start()
        # track time elapsed
        timestamp = datetime.datetime.now()
        for pdf in dataset.pdfs[:1]:
            parser.extract(pdf)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # calculate and record speed (PDFs per second)
        seconds_elapsed =  (datetime.datetime.now() - timestamp).total_seconds()
        parser.metrics.speed = "n/a" if seconds_elapsed == 0 else num_pdfs / seconds_elapsed
        # record memory usage (MB)
        parser.metrics.memory_usage = "n/a" if current < .01 else current / 10**6
    return
