import pandas as pd
from datetime import datetime

def log_progress(message):
    with open("code_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now().isoformat()} - {message}\n")

# First check the column names of each table

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
tables = pd.read_html(url, header=0)

print(f"Number of tables found: {len(tables)}")
# for idx, table in enumerate(tables):
#     print(f"Table {idx} columns: {list(table.columns)}")
    
    
# Extract the second table (index 1) and check its columns
def extract():
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    log_progress("Starting data extraction from Wikipedia")
    tables = pd.read_html(url)
    table = tables[1]
    print("Actual columns:", list(table.columns))  # Debug: See actual column names

    # Find columns by lowercased, stripped names
    # col_map = {col.strip().lower(): col for col in table.columns}
    # name_col = col_map.get("bank name")
    # mc_col = col_map.get("market cap (us$ billion)")
    # if name_col and mc_col:
    #     df = table[[name_col, mc_col]].copy()
    #     df = df.rename(columns={name_col: "Name", mc_col: "MC_USD_Billion"})
    #     log_progress("Data extraction complete")
    #     return df
    # else:
    #     log_progress("Could not find required columns")
    #     raise KeyError(f"Could not find columns: {col_map}")

extract()
