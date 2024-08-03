import os
import datetime
import tracemalloc

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
    pdfs = []
    Arxiv_papaers_directory = "dataset/Arxiv_papers"
    Arxiv_files = os.listdir(Arxiv_papaers_directory)
    for pdf in Arxiv_files:
        pdfs.append(Arxiv_papaers_directory+"/"+pdf)
    public_SEC_docs_directory = "dataset/public_SEC_docs"
    public_SEC_pdfs = os.listdir(public_SEC_docs_directory)
    for pdf in public_SEC_pdfs:
        pdfs.append(public_SEC_docs_directory+"/"+pdf)
    return pdfs

def retrieve_data(test_pdf_parsers, pdfs):
    #retrieve data for each pdf, track speed & memory usage
    num_pdfs = len(pdfs)
    for parser in test_pdf_parsers:
        parser.metrics = metrics()
        # track memory usage
        tracemalloc.start()
        # track time elapsed
        timestamp = datetime.datetime.now()
        for pdf in pdfs:
            parser.extract(pdf)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # calculate and record speed (PDFs per second)
        seconds_elapsed =  (datetime.datetime.now() - timestamp).total_seconds()
        parser.metrics.speed = "n/a" if seconds_elapsed == 0 else num_pdfs / seconds_elapsed
        # record memory usage (MB)
        parser.metrics.memory_usage = "n/a" if current < .01 else current / 10**6
    return

def output_evaluations(pdf_parsers):
    output_file = open("evaluations.txt", "w")
    for parser in pdf_parsers:
        output_file.write(parser.name + "\n")
        output_file.write("Speed: " + str(parser.metrics.speed)[:5] + " PDFs per second\n")
        output_file.write("Memory Usage: " + str(parser.metrics.memory_usage) + " MB\n")
        output_file.write("Accuracy: " + parser.metrics.accuracy + "\n")
        output_file.write("Cost: " + parser.metrics.cost + "\n\n")