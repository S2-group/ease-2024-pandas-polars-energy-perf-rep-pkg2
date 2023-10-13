import polars as pl
import numpy as np

# Load the DataFrame from the CSV file
df = pl.read_csv('Data/big_dataset.csv')

# Generate a time series in Polars
start_date = "2023-01-01"
end_date = "2023-01-10"
date_range = pl.date_range(start=start_date, end=end_date)

# Generate random time series data
pl.seed(0)
random_dates = date_range.sample(len(df), replace=True)

# Add the random time series as a new column
df = df.with_column(random_time_series=random_dates)
