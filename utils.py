import os
import datetime
import tracemalloc

class metrics:
    speed = 0
    memory_usage = 0
    cost = 0
    accuracy = 0
    variation_robustness = 0
    weights = {"speed": 10, "memory_usage": -1, "cost": -1, "accuracy": 10000, "variation_robustness": 0}
    weighted_score = 0

class result:
    extracted_data = ""
    parser = ""
    pdf = ""
    evaluation = ""

# get pdfs from dataset folder
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

# get text data from each pdf, record speed & memory usage
def retrieve_data(pdf_parsers, pdfs):
    text_data = {}
    num_pdfs = len(pdfs)
    for parser in pdf_parsers:
        # track memory & start time
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
        parser.metrics.memory_usage = 1000 if memory_usage < .1 else memory_usage 
        text_data[parser.name] = parser_text_data

        # record speed (PDFs per second)
        seconds_elapsed =  (datetime.datetime.now() - timestamp).total_seconds()
        parser.metrics.speed = 0 if seconds_elapsed == 0 else num_pdfs / seconds_elapsed
    return text_data

# record manual evaluation metrics cost and accuracy
def evaluate_parsers(pdf_parsers):
    for parser in pdf_parsers:
        evaluation = parser.evaluate()
        parser.metrics.cost = evaluation["Cost"]
        parser.metrics.accuracy = evaluation["Accuracy"]

# write text data to files in the output folder
def output_text(text_data):
    for parser in text_data:
        for pdf in text_data[parser]:
            output_dir = "output/"+pdf[:-4]
            os.makedirs(output_dir, exist_ok=True)
            output_file = open(output_dir + "/" + parser + ".txt", "w", encoding='utf-8')
            output_file.write(text_data[parser][pdf])

# write weighted scores and metrics to evaluations.txt
def output_evaluations(pdf_parsers):
    output_file = open("evaluations/evaluations.txt", "w")
    pdf_parsers.sort(key = lambda x : x.metrics.weighted_score, reverse=True)
    output_file.write("Weighted Scores:\n")
    for parser in pdf_parsers:
        output_file.write(parser.name + " "*(30-len(parser.name)))
        output_file.write(str(parser.metrics.weighted_score) + "\n")
    for parser in pdf_parsers:
        output_file.write("\n" + parser.name + "\n")
        output_file.write("Speed: " + str(parser.metrics.speed)[:5] + " PDFs per second\n")
        output_file.write("Memory Usage: " + str(parser.metrics.memory_usage) + " MB\n")
        output_file.write("Accuracy: " + str(parser.metrics.accuracy) + "\n")
        output_file.write("Cost: " + str(parser.metrics.cost) + "\n")
        output_file.write("Weighted Score: " + str(parser.metrics.weighted_score) + "\n")

# write speed metric to speed_comparison.txt
def compare_speed(pdf_parsers):
    output_file = open("evaluations/speed_comparison.txt", "w")
    pdf_parsers.sort(key=lambda x: float(x.metrics.speed), reverse=True)
    for parser in pdf_parsers:
        output_file.write(parser.name + " "*(30-len(parser.name)))
        output_file.write("Speed: " + str(parser.metrics.speed)[:5] + " PDFs per second\n")

# write memory usage metric to Memory_usage_comparison.txt
def compare_memory_usage(pdf_parsers):
    output_file = open("evaluations/memory_usage_comparison.txt", "w")
    pdf_parsers.sort(key=lambda x: float(x.metrics.memory_usage))
    for parser in pdf_parsers:
        if parser.name in ["Tabula Py", "camelot"]:
            parser.metrics.memory_usage = 1000
        output_file.write(parser.name + " "*(30-len(parser.name)))
        output_file.write("Memory usage: " + str(parser.metrics.memory_usage) + " MB\n")

# write accuracy metric to accuracy_comparison.txt
def compare_accuracy(pdf_parsers):
    output_file = open("evaluations/accuracy_comparison.txt", "w")
    pdf_parsers.sort(key=lambda x: float(x.metrics.memory_usage))
    for parser in pdf_parsers:
        output_file.write(parser.name + " "*(30-len(parser.name)))
        output_file.write("Accuracy: " + str(parser.metrics.accuracy) + " out of 1\n")

# calculate and record weighted scores
def compute_weighted_scores(pdf_parsers):
    for parser in pdf_parsers:
        weights = parser.metrics.weights
        speed = parser.metrics.speed
        memory_usage = parser.metrics.memory_usage
        cost = parser.metrics.cost
        accuracy = parser.metrics.accuracy
        parser.metrics.weighted_score = speed * weights["speed"] + \
                                        memory_usage * weights["memory_usage"] + \
                                        cost * weights["cost"] + \
                                        accuracy * weights["accuracy"] + 1000

# calculate and record a normalized version of the scores
def normalize_weighted_scores(pdf_parsers):
    scores = [parser.metrics.weighted_score for parser in pdf_parsers]
    OldMax = max(scores) + 1000
    OldMin = min(scores)
    NewMax = 100
    NewMin = 0
    OldRange = OldMax - OldMin
    NewRange = NewMax - NewMin
    for parser in pdf_parsers:
        OldValue = parser.metrics.weighted_score
        parser.metrics.weighted_score = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

        
        
