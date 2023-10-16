import pandas as pd
import numpy as np

small_ds_size = 1000


start_date = "2023-01-01"
end_date = "2033-01-10"
date_range = pd.date_range(start=start_date, end=end_date)


df = pd.read_csv('../../../../Data/big_dataset.csv',nrows=small_ds_size)


# Generate random time series data
np.random.seed(0)
random_dates = np.random.choice(date_range, size=len(df))



# Add the random time series as a new column
df['random_time_series'] = random_dates
