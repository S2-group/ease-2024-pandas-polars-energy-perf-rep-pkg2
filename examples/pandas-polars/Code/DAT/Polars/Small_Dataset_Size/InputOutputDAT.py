import polars as pl

small_ds_size = 1000
# Read csv dataset
def load_csv(path):
    return pl.read_csv(path,n_rows=small_ds_size)


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

def InputOutputDAT():
    folder = './OUTPUT_FILES'
    # # Read operations
    df = load_json(path=f"{folder}/Polars_Big.json")

    df = load_csv(path='../../../../Data/big_dataset.csv')
    df = load_parquet(path=f"{folder}/Polars_Big.parquet")

    save_csv(df, f'{folder}/df_adult_pandas_1.csv')
    save_json(df, f'{folder}/df_adult_pandas_1.json')
    save_parquet(df, f'{folder}/df_adult_pandas_1.parquet')
