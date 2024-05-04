
class dataset:
    pdfs = []

class retrieval:
    def extract(self, pdf, pdf_parser):
        return pdf_parser.extract(pdf)

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

class result:
    extracted_data = ""
    parser = ""
    pdf = ""
    evaluation = ""