from FileTypes import FileTypes
from InputOutputDAT import InputOutputDAT
from MissingDataDAT import MissingDataDAT
from StatisticalAggregationMinMaxUnique import StatisticalAggregationMinMaxUnique
from StatisticalAggregationSumMeanDAT import StatisticalAggregationSumMeanDAT
from ViewData import ViewData
import os, shutil

# Specify the desired working directory

def execute_files(n_times):
    for i in range(n_times):
        current_directory = os.getcwd()
        print("Current Working Directory:", current_directory)
        output_files = './examples/pandas-polars/Code/DAT/Pandas/Small_Dataset_Size/OUTPUT_FILES'
        data_files = './examples/pandas-polars/Data/big_dataset.csv'


        # for i in range(n_times):
        #     for filename in os.listdir(output_files):
        #         file_path = os.path.join(output_files, filename)
        #         try:
        #             if os.path.isfile(file_path) or os.path.islink(file_path):
        #                 os.unlink(file_path)
        #             elif os.path.isdir(file_path):
        #                 shutil.rmtree(file_path)
        #         except Exception as e:
        #             print('Failed to delete %s. Reason: %s' % (file_path, e))
        FileTypes(output_files, data_files)
        MissingDataDAT(output_files, data_files)
        StatisticalAggregationMinMaxUnique(output_files, data_files)
        StatisticalAggregationSumMeanDAT(output_files, data_files)
        ViewData(output_files, data_files)
        InputOutputDAT(output_files, data_files)


execute_files(10)


        