import polars as pl


def drop(df, cnameArray):
    return df.drop(columns=cnameArray)


def groupby(df, cname):
    return df.group_by(cname).count()


## do we want to do count?? -- doesn't do the same thing as pandas?


# def merge(df1, df2, on=None):



def sort(df, cname):
    return df.sort(cname)


def concat_dataframes(df1, df2):
    return pl.concat([df1, df2])


# # Row Column Operations

df = pl.read_csv('/Users/apoorvanp/GreenLab-Code-Repo/goGreen/Data/big_dataset.csv')
df_samp = pl.read_csv('/Users/apoorvanp/GreenLab-Code-Repo/goGreen/Data/big_dataset.csv')

# print(drop(df, cnameArray=['Professional', 'Unemployment']))
# groupby(df, cname='State')


SAMPLE_SIZE = 20000
df_samp = df.sample(SAMPLE_SIZE)
concat_dataframes(df, df_samp)
sort(df, 'VotingAgeCitizen')

## need to write merge/join

