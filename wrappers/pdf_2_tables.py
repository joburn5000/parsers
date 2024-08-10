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
    return "pdf2tables is out of date"
    # return tables


def evaluate():
    evaluation = {"Cost": 0, "Accuracy": 0}
    return evaluation