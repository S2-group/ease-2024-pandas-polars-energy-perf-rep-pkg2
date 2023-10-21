
import pandas as pd

def StatisticalAggregationMinMaxUnique(output_files,data_files):

    df = pd.read_csv(data_files)


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


for i in range(400):
    output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
    small_data_files = './examples/pandas-polars/Data/final_small_dataset.csv'
    StatisticalAggregationMinMaxUnique(output_files, small_data_files)
