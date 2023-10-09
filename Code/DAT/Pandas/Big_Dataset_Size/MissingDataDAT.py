# Handling missing data

import pandas as pd

############## COUNT MISSING VALUES AND REMOVE THEM ###############

df = pd.read_csv('Data/big_dataset.csv')
df_drop = df.copy()
df_fill = df.copy()

# Check for missing data before manipulation
missing_counts_before_drop = df_drop.isnull().sum().sum()

# drop missing data
df_drop.dropna(inplace=True)

# Check for missing data before manipulation
missing_counts_after_drop = df_drop.isnull().sum().sum()

############## COUNT MISSING VALUES AND REMOVE THEM ###############

#count_ones_before_fill = (df_fill == 1).values.sum()

# Fill None with 0
df_fill.fillna(1, inplace=True) 

# Check for missing data (None values)
missing_counts_after_fill = df_fill.isnull().sum().sum()

#count_ones_after_fill = (df_fill == 1).values.sum()

print(f"Missing Counts before Drop: {missing_counts_before_drop},"+
       f"\nAFTER: {missing_counts_after_drop}"+
           f"\nNULLS AFTER FILL: {missing_counts_after_fill}")
