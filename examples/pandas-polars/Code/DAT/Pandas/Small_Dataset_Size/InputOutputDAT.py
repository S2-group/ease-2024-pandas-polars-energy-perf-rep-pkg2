import os
import pandas as pd

small_ds_size = 1000

def InputOutputDAT(output_files, data_file):

    # Read csv dataset
    def load_csv(path):
        return pd.read_csv(path,nrows=small_ds_size)


    # Read parquet dataset
    def load_parquet(path):
        return pd.read_parquet(path, engine='pyarrow')


    # Read json dataset
    def load_json(path):
        return pd.read_json(path, nrows=small_ds_size, lines=True)


    def save_csv(df, path):
        return df.to_csv(path)


    def save_json(df, path):
        return df.to_json(path)


    def save_parquet(df, path):
        return df.to_parquet(path)

    PandasSmall_json = os.path.join(output_files, "Pandas_Big.json")
    PandasSmall_parquet = os.path.join(output_files, "Pandas_Big.parquet")
    # # Read operations
    df = load_json(PandasSmall_json)

    df = load_csv(data_file)

    df = load_parquet(PandasSmall_parquet)

    new_Csv = os.path.join(output_files, "df_adult_pandas_1.csv")
    new_JSON = os.path.join(output_files, "df_adult_pandas_1.json")
    new_parque = os.path.join(output_files, "df_adult_pandas_1.parquet")

    save_csv(df, new_Csv)
    save_json(df, new_JSON)
    save_parquet(df, new_parque)
