import pandas as pd
from datetime import datetime

# Funcion to log progress messages to a file
def log_progress(message):
    with open("code_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now().isoformat()} - {message}\n")

# First check the column names of each table
url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
tables = pd.read_html(url, header=0)
       
# Extract the second table (index 1)
def extract():
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    log_progress("Starting data extraction from Wikipedia")
    tables = pd.read_html(url)
    table = tables[1]
    print("Table 1 columns:", list(table.columns))  # Debug: See actual column names

# Extract the data under the heading 'By market capitalization' and save it to a dataframe.
    df = table[["Bank name", "Market cap (US$ billion)"]].copy()
    df = df.rename(columns={"Bank name": "Name", "Market cap (US$ billion)": "MC_USD_Billion"})
    log_progress("Data extraction complete")
    return df

if __name__ == "__main__":
    extracted_data = extract()
    print(extracted_data)  # Verify output
    log_progress("Extraction function executed and output verified")

# Upload the image ‘Task_3a_transform.png’. This should show the code for the function ‘transform’ used in the project. (1 point)
# Function to transform the data
def transform(df):
    log_progress("Starting data transformation")
    # Convert Market Cap to numeric and handle errors
    df["MC_USD_Billion"] = pd.to_numeric(df["MC_USD_Billion"], errors="coerce")
    # Drop rows with NaN values
    df = df.dropna()
    log_progress("Data transformation complete")
    return df
