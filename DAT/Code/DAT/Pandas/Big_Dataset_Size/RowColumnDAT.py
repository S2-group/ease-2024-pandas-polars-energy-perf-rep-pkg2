import pandas as pd


def drop(df, cnameArray):
    return df.drop(columns=cnameArray)


def groupby(df, cname):
    print(df.groupby(cname).agg('count'))
    return df.groupby(cname).agg('count')


## do we wanna do count??


def merge(df1, df2, on=None):
    # KARO - I used pd.concat with an "outer" join to concatenate the two DataFrames along the rows. 
    # This operation allows duplications and combines all rows from both DataFrames.
    # I THINK IT IS BETTER THAN merge with if but let's talk
    return pd.concat([df1, df2], axis=0, ignore_index=True)
    
    # if on:
    #     return pd.merge(df1, df2, on=on)
    # else:
    #     return pd.merge(df1, df2)


def sort(df, cname):
    return df.sort_values(by=[cname])


def concat_dataframes(df1, df2):
    return pd.concat([df1, df2])


# # Row Column Operations

df = pd.read_csv('Data/big_dataset.csv')
df_samp = pd.read_csv('Data/big_dataset.csv')
drop(df, cnameArray=['Professional', 'Unemployment'])
groupby(df, cname='State')
SAMPLE_SIZE = 20000
df_samp = df.sample(SAMPLE_SIZE)
concat_dataframes(df, df_samp)
sort(df, 'VotingAgeCitizen')
merge(df, df_samp)
