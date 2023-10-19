# Converting different filetypes
import os, shutil
import polars as pl

def FileTypes(output_files, data_file):

    # Load the CSV file into a Polars DataFrame
    df = pl.read_csv(data_file)

    PolarsBig_json = os.path.join(output_files, "Polars_Big.json")
    PolarsBig_parquet = os.path.join(output_files, "Polars_Big.parquet")

    # Convert the DataFrame to JSON format
    df.write_json(PolarsBig_json)  # Converts each row to a JSON object

    df.write_parquet(PolarsBig_parquet)  # Converts each row to a JSON object
