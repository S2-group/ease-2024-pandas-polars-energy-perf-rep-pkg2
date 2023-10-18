import polars as pl

# Define a function to find the minimum value of all columns
def min(df: pl.DataFrame):
    return df.min()

# Define a function to find the maximum value of all columns
def max(df: pl.DataFrame):
    return df.max()

# Define a function to find unique values in a column
def unique(df: pl.DataFrame):
    return df.unique(maintain_order=True)

def StatisticalAggregationMinMaxUnique():
    # Perform statistical operations
    df = pl.read_csv('Data/big_dataset.csv')
    MinIncome = min(df['Income'])
    MaxIncome = max(df['Income'])
    States = unique(df['State'])

    # Print the results
    print(f" MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")