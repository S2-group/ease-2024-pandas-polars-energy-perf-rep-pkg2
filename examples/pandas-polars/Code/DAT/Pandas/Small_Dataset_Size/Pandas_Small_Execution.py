from FileTypes import FileTypes
from InputOutputDAT import InputOutputDAT
from MissingDataDAT import MissingDataDAT
from StatisticalAggregationMinMaxUnique import StatisticalAggregationMinMaxUnique
from StatisticalAggregationSumMeanDAT import StatisticalAggregationSumMeanDAT
from ViewData import ViewData

file_names = [
    'FileTypes.py',
    'InputOutputDAT.py',
    'MissingDataDAT.py',
    'StatisticalAggregationMinMaxUnique.py',
    'StatisticalAggregationSumMeanDAT.py',
    'TimeSeriesDAT.py',
    'ViewData.py'
    ]

def execute_files(n_times):
    for i in n_times:
        FileTypes()
        InputOutputDAT()
        MissingDataDAT()
        StatisticalAggregationMinMaxUnique()
        StatisticalAggregationSumMeanDAT()
        ViewData()


        