
import pandas as pd

df = pd.read_csv('Data/big_dataset.csv')


# min
def min(df:pd.DataFrame):
    return df.min()
# max
def max(df:pd.DataFrame):
    return df.max()

# unique
def unique(df:pd.DataFrame):
    return df.unique()

### Statistical Operations


MinCommute = min(df['MeanCommute'])
MaxCommute = max(df['MeanCommute'])
States = unique(df['MeanCommute'])

print(f"\n MinCommute: {MinCommute},\n MaxCommute: {MaxCommute},\n States: {States}")
