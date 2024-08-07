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

def retrieve_data(pdf_parsers, pdfs):
    #retrieve data for each pdf, track speed & memory usage
    text_data = {}
    num_pdfs = len(pdfs)
    for parser in pdf_parsers:
        # track memory usage & start time
        tracemalloc.start()
        timestamp = datetime.datetime.now()

        # extract text
        parser_text_data = {}
        for pdf in pdfs:
            parser_text_data[pdf] = parser.extract(pdf)
        
        # record memory usage (MB)
        memory_usage = tracemalloc.get_traced_memory()[0] / 10**6
        tracemalloc.stop()
        parser.metrics = metrics()
        parser.metrics.memory_usage = "100000" if memory_usage < .1 else memory_usage 
        text_data[parser.name] = parser_text_data

        # record speed (PDFs per second)
        seconds_elapsed =  (datetime.datetime.now() - timestamp).total_seconds()
        parser.metrics.speed = "0" if seconds_elapsed == 0 else num_pdfs / seconds_elapsed
    return text_data

def evaluate_parsers(pdf_parsers):
    for parser in pdf_parsers:
        evaluation = parser.evaluate()
        parser.metrics.cost = evaluation["Cost"]

def output_text(text_data):
    for parser in text_data:
        for pdf in text_data[parser]:
            output_dir = "output/"+pdf[:-4]
            os.makedirs(output_dir, exist_ok=True)
            output_file = open(output_dir + "/" + parser + ".txt", "w", encoding='utf-8')
            output_file.write(text_data[parser][pdf])

            
def output_evaluations(pdf_parsers):
    output_file = open("evaluations/evaluations.txt", "w")
    for parser in pdf_parsers:
        output_file.write(parser.name + "\n")
        output_file.write("Speed: " + str(parser.metrics.speed)[:5] + " PDFs per second\n")
        output_file.write("Memory Usage: " + str(parser.metrics.memory_usage) + " MB\n")
        output_file.write("Accuracy: " + parser.metrics.accuracy + "\n")
        output_file.write("Cost: " + parser.metrics.cost + "\n\n")

def compare_speed(pdf_parsers):
    output_file = open("evaluations/speed_comparison.txt", "w")
    pdf_parsers.sort(key=lambda x: float(x.metrics.speed), reverse=True)
    for parser in pdf_parsers:
        output_file.write(parser.name + " "*(30-len(parser.name)))
        output_file.write("Speed: " + str(parser.metrics.speed)[:5] + " PDFs per second\n")

def compare_memory_usage(pdf_parsers):
    output_file = open("evaluations/memory_usage_comparison.txt", "w")
    pdf_parsers.sort(key=lambda x: float(x.metrics.memory_usage))
    for parser in pdf_parsers:
        if parser.name in ["Tabula Py", "camelot"]:
            parser.metrics.memory_usage = 100000
        output_file.write(parser.name + " "*(30-len(parser.name)))
        output_file.write("Memory usage: " + str(parser.metrics.memory_usage) + " MB\n")