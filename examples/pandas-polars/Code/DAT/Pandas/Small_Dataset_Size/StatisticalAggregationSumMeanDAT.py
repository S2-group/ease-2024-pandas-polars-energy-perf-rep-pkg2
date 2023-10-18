
import pandas as pd

def StatisticalAggregationSumMeanDAT():

    small_ds_size = 1000

    df = pd.read_csv('../../../../Data/big_dataset.csv',nrows=small_ds_size)

    def count(df:pd.DataFrame):
        return df.count(axis=0)

    # sum
    def sum(df:pd.DataFrame):
        return df.sum()

    # mean
    def mean(df:pd.DataFrame):
        return df.mean()



    ### Statistical Operations
    dfCount = count(df)
    summedIncome = sum(df['Income'])
    MeanIncome = mean(df['Income'])


    print(f"{dfCount}\nsummedIncome: {summedIncome},\n MeanIncome: {MeanIncome}")