# Converting different filetypes
import os, shutil
import pandas as pd

def FileTypes(output_files, data_files):

    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(data_files)

    PandasBig_json = os.path.join(output_files, "Pandas_Big.json")
    PandasBig_parquet = os.path.join(output_files, "Pandas_Big.parquet")

    # Convert the DataFrame to JSON format
    df.to_json(PandasBig_json)  # Converts each row to a JSON object

    # Convert the DataFrame to parquet format
    df.to_parquet(PandasBig_parquet)