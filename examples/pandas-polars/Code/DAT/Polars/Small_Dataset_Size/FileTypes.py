# Converting different filetypes
import os, shutil
import polars as pl

def FileTypes(output_files, data_file):
    small_ds_size = 1000

    # Load the CSV file into a Polars DataFrame
    df = pl.read_csv(data_file,n_rows=small_ds_size)

    PolarsSmall_json = os.path.join(output_files, "Polars_Small.json")
    PolarsSmall_parquet = os.path.join(output_files, "Polars_Small.parquet")

    # Convert the DataFrame to JSON format
    df.write_json(PolarsSmall_json)  # Converts each row to a JSON object

    df.write_parquet(PolarsSmall_parquet)  # Converts each row to a JSON object
