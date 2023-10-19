from FileTypes import FileTypes
from InputOutputDAT import InputOutputDAT
from MissingDataDAT import MissingDataDAT
from StatisticalAggregationMinMaxUnique import StatisticalAggregationMinMaxUnique
from StatisticalAggregationSumMeanDAT import StatisticalAggregationSumMeanDAT
from ViewData import ViewData
import os, shutil

# Specify the desired working directory

def execute_files(n_times):
    current_directory = os.getcwd()
    print("Current Working Directory:", current_directory)
    folder = './Code/DAT/Pandas/Big_Dataset_Size/OUTPUT_FILES'

    for i in range(n_times):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        FileTypes()
        # MissingDataDAT()
        # StatisticalAggregationMinMaxUnique()
        # StatisticalAggregationSumMeanDAT()
        # ViewData()
        # InputOutputDAT()


execute_files(10)


        