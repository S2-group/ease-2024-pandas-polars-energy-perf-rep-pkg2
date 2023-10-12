import polars as pl


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


# # Read operations
df = load_json(path='/Users/apoorvanp/GreenLab-Code-Repo/goGreen/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
                    '/Pandas_Big.json')

df = load_csv(path='/Users/apoorvanp/GreenLab-Code-Repo/goGreen/Data/big_dataset.csv')
df = load_parquet(path='/Users/apoorvanp/GreenLab-Code-Repo/goGreen/Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'
                       '/Pandas_Big.parquet')

save_csv(df, f'df_adult_pandas_1.csv')
save_json(df, f'df_adult_pandas_1.json')
save_parquet(df, f'df_adult_pandas_1.parquet')
