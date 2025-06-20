from datetime import datetime

import pandas as pd
import requests

def log_progress(message):
    with open("code_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")


# Task 2:
# Extract the tabular information from the given URL under the heading 'By market capitalization' and save it to a dataframe.
# a. Inspect the webpage and identify the position and pattern of the tabular information in the HTML code
# b. Write the code for a function extract() to perform the required data extraction.
# c. Execute a function call to extract() to verify the output.

def extract():
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    tables = pd.read_html(url, match="Market capitalization")
    df = tables[0][["Name", "Market cap(US$ billion)"]]
    df.columns = ["Name", "MC_USD_Billion"]
    log_progress("Data extracted from Wikipedia")
    return df
