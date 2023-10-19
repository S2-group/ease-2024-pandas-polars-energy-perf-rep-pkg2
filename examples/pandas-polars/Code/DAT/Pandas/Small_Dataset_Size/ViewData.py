import pandas as pd

def ViewData():

    small_ds_size = 1000
    # Create a sample DataFrame
    df = pd.read_csv('../../../../Data/big_dataset.csv',nrows=small_ds_size)

    # Display the DataFrame
    print("Pandas: Display DataFrame using head()")
    print(df.head())

    print("\nPandas: Display DataFrame using tail()")
    print(df.tail())

    print("\nPandas: Display DataFrame dtypes")
    print(df.dtypes)

    print("\nPandas: Display DataFrame describe()")
    print(df.describe())

    print("\nPandas: Display DataFrame shape")
    print(df.shape)
