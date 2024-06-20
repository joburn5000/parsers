
class dataset:
    pdfs = []

class metrics:
    # init TODO
    speed = ""
    resource_efficiency = ""
    cost = ""
    accuracy = ""
    variation_robustness = ""

class pdf_parser:
    type = ""
    extract = ""
    metrics = metrics()
    result = result()

class result:
    extracted_data = ""
    parser = ""
    pdf = ""
    evaluation = ""