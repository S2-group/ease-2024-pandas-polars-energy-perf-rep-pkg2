# Converting different filetypes
import os, shutil
import pandas as pd

def FileTypes():
    folder = './Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'

    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv('./Data/big_dataset.csv')

    # Convert the DataFrame to JSON format
    df.to_json(f"{folder}/Pandas_Big.json")  # Converts each row to a JSON object

    # Convert the DataFrame to parquet format
    df.to_parquet(f"{folder}/Pandas_Big.parquet")