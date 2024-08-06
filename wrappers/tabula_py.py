# tabula_py https://github.com/chezou/tabula-py 
import tabula
import os
name = "Tabula Py"

# todo test tabula
def extract(pdf):
    output_dir = "output/"+pdf[:-4]
    os.makedirs(output_dir, exist_ok=True)
    output_file = open(output_dir+"/tabula.txt", "w", encoding='utf-8')
    # Read pdf into list of DataFrame
    dfs = tabula.read_pdf(pdf, pages='all')
    # convert PDF into CSV file
    tabula.convert_into(pdf, "tabula_output.csv", output_format="csv", pages='all')
    # notes: extracts TABLE data to a CSV format. dependency (not necessary to run it though) jpype 'pip install jpype1'
    for df in dfs:
        output_file.write(str(df))
    return dfs


def evaluate():
    evaluation = {"Cost": "Free", "Variation Robustness": "n/a"}
    return evaluation