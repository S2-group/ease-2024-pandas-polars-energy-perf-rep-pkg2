import polars as pl

# Load the CSV data into a Polars DataFrame
df = pl.read_csv('Data/big_dataset.csv')

# Define a function to count missing values
def count(df: pl.DataFrame):
    return df.select(pl.all().is_not_null().sum())


# Define a function to calculate the sum of a column
def sum(df: pl.DataFrame):
    return df.sum()

# Define a function to calculate the mean of all columns
def mean(df: pl.DataFrame):
    return df.mean()

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
dfCount = count(df)
summedIncome = sum(df['Income'])
MeanIncome = mean(df['Income'])
MinIncome = min(df['Income'])
MaxIncome = max(df['Income'])
States = unique(df['State'])

# Print the results
print(f"{dfCount}\nsummedIncome: {summedIncome},\n MeanIncome: {MeanIncome},\n MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")