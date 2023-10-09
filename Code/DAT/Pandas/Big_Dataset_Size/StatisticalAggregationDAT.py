
import pandas as pd

############## COUNT MISSING VALUES AND REMOVE THEM ###############

df = pd.read_csv('Data/big_dataset.csv')

def count(df:pd.DataFrame):
    return df.count(axis=0)

# sum
def sum(df:pd.DataFrame):
    return df.sum()

# mean
def mean(df:pd.DataFrame):
    return df.mean()

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
dfCount = count(df)
summedIncome = sum(df['Income'])
MeanIncome = mean(df['Income'])
MinIncome = min(df['Income'])
MaxIncome = max(df['Income'])
States = unique(df['State'])

print(f"{dfCount}\nsummedIncome: {summedIncome},\n MeanIncome: {MeanIncome},\n MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")