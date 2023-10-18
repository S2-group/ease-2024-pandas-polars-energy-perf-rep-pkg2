import polars as pl

def StatisticalAggregationMinMaxUnique():
    small_ds_size = 1000
    # Load the CSV data into a Polars DataFrame
    df = pl.read_csv('Data/big_dataset.csv', small_ds_size)


    # Define a function to find the minimum value of all columns
    def min(df: pl.DataFrame):
        return df.min()

    # Define a function to find the maximum value of all columns
    def max(df: pl.DataFrame):
        return df.max()

    # Define a function to find unique values in a column
    def unique(df: pl.DataFrame):
        return df.unique(maintain_order=True)

    # Perform statistical operations

    MinIncome = min(df['Income'])
    MaxIncome = max(df['Income'])
    States = unique(df['State'])

    # Print the results
    print(f" MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")