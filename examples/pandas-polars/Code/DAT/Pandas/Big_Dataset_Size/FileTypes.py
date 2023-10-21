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


for i in range(15):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    FileTypes(output_files, big_data_files)