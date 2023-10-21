import os
import pandas as pd

def InputOutputDAT(output_files, data_file):
    # Read csv dataset
    def load_csv(path):
        return pd.read_csv(path)


    # Read parquet dataset
    def load_parquet(path):
        print("Inside load parquet")
        return pd.read_parquet(path, engine='pyarrow')


    # Read json dataset
    def load_json(path):
        print("Inside load json")
        return pd.read_json(path)


    def save_csv(df, path):
        print("Inside load csv")
        return df.to_csv(path)


    def save_json(df, path):
        print("Inside save json")
        return df.to_json(path)


    def save_parquet(df, path):
        print("Inside save parquet")
        return df.to_parquet(path)

    # # Read operations
    print("Before read operations")
    PandasBig_json = os.path.join(output_files, "Pandas_Big.json")
    PandasBig_parquet = os.path.join(output_files, "Pandas_Big.parquet")

    jdf = load_json(path=PandasBig_json)

    cdf = load_csv(path=data_file)

    pdf = load_parquet(path=PandasBig_parquet)

    print("After load operations")

    new_Csv = os.path.join(output_files, "df_adult_pandas_1.csv")
    new_JSON = os.path.join(output_files, "df_adult_pandas_1.json")
    new_parque = os.path.join(output_files, "df_adult_pandas_1.parquet")

    print("Before save")
    save_csv(cdf, new_Csv)
    save_json(jdf, new_JSON)
    save_parquet(pdf, new_parque)
    print("After Save")


for i in range(1):
    print(" I am inside for loop")
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
    big_data_files = './examples/pandas-polars/Data/final_big_dataset.csv'
    InputOutputDAT(output_files, big_data_files)
