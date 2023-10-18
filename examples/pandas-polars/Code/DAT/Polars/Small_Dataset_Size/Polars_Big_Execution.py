from FileTypes import FileTypes
from InputOutputDAT import InputOutputDAT
from MissingDataDAT import MissingDataDAT
from StatisticalAggregationMinMaxUnique import StatisticalAggregationMinMaxUnique
from StatisticalAggregationSumMeanDAT import StatisticalAggregationSumMeanDAT
from ViewData import ViewData

def execute_files(n_times):
    for i in n_times:
        FileTypes()
        InputOutputDAT()
        MissingDataDAT()
        StatisticalAggregationMinMaxUnique()
        StatisticalAggregationSumMeanDAT()
        ViewData()

execute_files(10)


        