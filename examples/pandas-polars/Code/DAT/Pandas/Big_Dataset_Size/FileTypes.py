# Converting different filetypes
import os, shutil
import pandas as pd

def FileTypes(folder, data_file):

    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(data_file)

    # Convert the DataFrame to JSON format
    df.to_json(f'./OUTPUT_FILES/Pandas_Big.json')  # Converts each row to a JSON object

    # Convert the DataFrame to parquet format
    df.to_parquet(f'./OUTPUT_FILES/Pandas_Big.parquet')