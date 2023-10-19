import polars as pl

def ViewData(output_files, data_file):
    # Create a sample DataFrame
    df = pl.read_csv(data_file)

    # Display the DataFrame
    print("Polars: Display DataFrame using head()")
    print(df.head())

    print("\nPolars: Display DataFrame using tail()")
    print(df.tail())

    print("\nPandas: Display DataFrame dtypes")
    print(df.dtypes)

    print("\nPolars: Display DataFrame describe()")
    print(df.describe())

    print("\nPolars: Display DataFrame shape")
    print(df.shape)
