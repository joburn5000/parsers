from pdf2tables import pdf_tables
import numpy as np
name = "pdf2tables"
# pdf2tables https://github.com/chen1tian/pdf2tables

def extract(pdf):
    # imgOcrSettings = {
    #         'pytesseract_kernel': np.ones((4, 4), np.uint8),
    #         'pytesseract_bin_threshold': 127,
    #         'pytesseract_iterations': 1,
    #         # 单元格面积范围，决定哪些单元格会被选中
    #         'pytesseract_areaRange': [10000, 100000],
    #         'pytesseract_isDebug': False,
    #         # 单元格边框，用来更精确地获取文本
    #         'pytesseract_border': 10,
    #         'aliyun_appcode': 'b8f41a5f9b664a45af2bc9f58666a17e'
    #     }
    # tables = pdf_tables.extract(pdf, lang='eng+tha', **imgOcrSettings)
    print("pdf2tables is out of date")
    # return tables

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
