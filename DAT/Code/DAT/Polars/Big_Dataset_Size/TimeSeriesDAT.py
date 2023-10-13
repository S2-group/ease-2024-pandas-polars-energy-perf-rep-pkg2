import polars as pl

# Generate a time series in Polars
start_date = "2023-01-01"
end_date = "2023-01-10"
date_range = pl.date_range(start=start_date, end=end_date)
print(date_range)