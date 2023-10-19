
import pandas as pd

def StatisticalAggregationMinMaxUnique():
    df = pd.read_csv('../../../../Data/big_dataset.csv')


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

    MinIncome = min(df['Income'])
    MaxIncome = max(df['Income'])
    States = unique(df['State'])

    print(f"\n MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")

