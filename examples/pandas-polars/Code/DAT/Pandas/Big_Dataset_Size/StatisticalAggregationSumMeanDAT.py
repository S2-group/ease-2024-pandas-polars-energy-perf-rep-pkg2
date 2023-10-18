
import pandas as pd

def StatisticalAggregationSumMeanDAT():
    df = pd.read_csv('../../../../Data/big_dataset.csv')

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