import os
import polars as pl

def InputOutputDAT(output_files, data_file):
    # Read csv dataset
    def load_csv(path):
        return pl.read_csv(path)


    # Read parquet dataset
    def load_parquet(path):
        return pl.read_parquet(path)


    # Read json dataset
    def load_json(path):
        return pl.read_json(path)


    def save_csv(df, path):
        return df.write_csv(path)


    def save_json(df, path):
        return df.write_json(path)


    def save_parquet(df, path):
        return df.write_parquet(path)

    PolarsBig_json = os.path.join(output_files, "Polars_Big.json")
    PolarsBig_parquet = os.path.join(output_files, "Polars_Big.parquet")

    # # Read operations
    df = load_csv(data_file)
    df = load_json(PolarsBig_json)
    df = load_parquet(PolarsBig_parquet)

    new_Csv = os.path.join(output_files, "df_adult_polars_1.csv")
    new_JSON = os.path.join(output_files, "df_adult_polars_1.json")
    new_parque = os.path.join(output_files, "df_adult_polars_1.parquet")

    save_csv(df, new_Csv)
    save_json(df, new_JSON)
    save_parquet(df, new_parque)


for i in range(400):
    output_files = './examples/pandas-polars/Code/DAT/Polars/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    InputOutputDAT(output_files, big_data_files)

