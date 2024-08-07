# tabula_py https://github.com/chezou/tabula-py 
import tabula
import os
name = "Tabula Py"

# todo test tabula
def extract(pdf):
    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf(pdf, pages='all')
    # convert PDF into CSV file
    tabula.convert_into(pdf, "tabula_output.csv", output_format="csv", pages='all')
    # notes: extracts TABLE data to a CSV format. dependency (not necessary to run it though) jpype 'pip install jpype1'
    text = ""
    for df in dfs:
        df_text = str(df)
    return text


def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation