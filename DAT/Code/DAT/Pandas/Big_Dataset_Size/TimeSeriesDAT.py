import pandas as pd

# Generate a time series in Pandas
start_date = "2023-01-01"
end_date = "2033-01-10"
date_range = pd.date_range(start=start_date, end=end_date)
print(date_range)