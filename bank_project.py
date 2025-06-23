import pandas as pd
from datetime import datetime
import sqlite3

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
    
# Transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places, 
# based on the exchange rate information shared as a CSV file.

def transform(df):
    # Load exchange rates
    exchange_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv"
    rates = pd.read_csv(exchange_url, index_col=0).squeeze("columns")
    # Ensure MC_USD_Billion is numeric
    df["MC_USD_Billion"] = pd.to_numeric(df["MC_USD_Billion"], errors="coerce")
    # Add new columns, rounded to 2 decimals
    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * rates["GBP"]).round(2)
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * rates["EUR"]).round(2)
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * rates["INR"]).round(2)
    log_progress("Data transformed with exchange rates")
    return df

if __name__ == "__main__":
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    print(transformed_data)  # Verify output
    log_progress("Transform function executed and output verified")
    
# Upload the image ‘Task_4_CSV.png’. This should be the contents of the CSV file created from the final table
# Load the transformed dataframe to an output CSV file: Output CSV Path	./Largest_banks_data.csv
def load_to_csv(df, output_path="./Largest_banks_data.csv"):
    df.to_csv(output_path, index=False)
    log_progress(f"Data loaded to CSV at {output_path}")

if __name__ == "__main__":
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load_to_csv(transformed_data)
    print("Data loaded to CSV successfully")
    log_progress("Load to CSV function executed and output verified")
    
# Load the transformed dataframe to an SQL database server as a table. 
# Write a function load_to_db(), execute a function call and verify the output.

def load_to_db(df, db_path="bank_data.db", table_name="largest_banks"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    log_progress(f"Data loaded to database at {db_path}, table: {table_name}")

if __name__ == "__main__":
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load_to_db(transformed_data)
    print("Data loaded to database successfully")
    log_progress("Load to DB function executed and output verified")