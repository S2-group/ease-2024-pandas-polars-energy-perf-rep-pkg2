# Converting different filetypes
import os, shutil
import polars as pl

def FileTypes():
    small_ds_size = 1000

    folder = './OUTPUT_FILES'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # Load the CSV file into a Polars DataFrame
    df = pl.read_csv('../../../../Data/big_dataset.csv',n_rows=small_ds_size)

    # Convert the DataFrame to JSON format
    df.write_json(f"{folder}/Polars_Big.json")  # Converts each row to a JSON object

    df.write_parquet(f"{folder}/Polars_Big.parquet")  # Converts each row to a JSON object
