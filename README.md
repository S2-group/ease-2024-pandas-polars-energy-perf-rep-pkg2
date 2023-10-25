# Pandas vs Polars: A Comparison of Energy Efficiency and Performance

[Visit Pandas](https://pandas.pydata.org/)
[Visit Polars](https://www.pola.rs/)
--- 
> The purpose of this study is to compare and evaluate the two
 dataframe libraries Pandas and Polars in terms of energy efficiency.
Polars has published a benchmark against several other solutions claiming
it has better performance in terms of speed when running different 
SQL queries, especially compared to Pandas6. Additionally,
there exist other benchmarks comparing the performance of Pandas
and Polars using different queries which report similar results.
Predominantly we will look whether the improved performance
that has been reported by Polars, translates into energy efficiency.
Our contribution specifically studies the energy impact of using
Pandas and Polars in different scenarios like dataset size, operations
performed as well as existance of any correlation between energy usage and performance in these two librairies.
Our project contains two experiments which can also be run separetly.  
1. Evaluating impact of eneregy efficiency within an official TPCB benchmarking from Polars [TPC website](https://www.tpc.org/tpch/)
2. Evaluating impact of eneregy efficiency with a set of commonly used data analysis tasks inspired by [This study](https://ieeexplore.ieee.org/document/10174114)

# Requirements

1. Before you begin, make sure you have Python 3 installed on your system. This project requires Python 3 to run. [Link to Inatall Python](https://www.python.org/downloads/)
2. Install the project requiremenst using the following:
```shell
pip install -r requirement.txt
```

# Running the project

- For running our experiment operating with differen data analysis tasks follow the steps provided in the [DAT Setup Section](examples/README.md#setup) 

- For running the TPCH experiment from Polars follow the steps provided in the [TPCH Setup Section](tpch-pandas-polars/README.md#setup)