
import pandas as pd

def StatisticalAggregationMinMaxUnique():

    small_ds_size = 1000

    df = pd.read_csv('../../../../Data/big_dataset.csv', nrows=small_ds_size)


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


    MinIncome = min(df['MeanIncome'])
    MaxIncome = max(df['MeanIncome'])
    States = unique(df['MeanIncome'])

    print(f"\n MinIncome: {MinIncome},\n MaxIncome: {MaxIncome},\n States: {States}")
