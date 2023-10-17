from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ExtendedTyping.Typing import SupportsStr
from ProgressManager.Output.OutputProcedure import OutputProcedure as output

from typing import Dict, List, Any, Optional
from pathlib import Path
from os.path import dirname, realpath

import subprocess
import signal
import time
import shlex
import os
import pandas as pd


class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name: str = "new_runner_experiment"

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path: Path = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type: OperationType = OperationType.AUTO

    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms: int = 1000

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""

        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN, self.before_run),
            (RunnerEvents.START_RUN, self.start_run),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT, self.interact),
            (RunnerEvents.STOP_MEASUREMENT, self.stop_measurement),
            (RunnerEvents.STOP_RUN, self.stop_run),
            (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT, self.after_experiment)
        ])
        self.run_table_model = None  # Initialized later

        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
        representing each run performed"""
        # factor1 = FactorModel("run_number", ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10'])
        # factor2 = FactorModel("library", ['Pandas', 'Polars'])
        factor3 = FactorModel("dataframe_size", ['Big', 'Small'])
        self.run_table_model = RunTableModel(
            factors=[factor3],
            # exclude_variations=[
            #     {factor1: ['example_treatment1']},                   # all runs having treatment "example_treatment1" will be excluded
            #     {factor1: ['example_treatment2'], factor2: [True]},  # all runs having the combination ("example_treatment2", True) will be excluded
            # ],
            data_columns=['avg_cpu', 'avg_mem', 'avg_exec_time', 'avg_energy']
        )
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""

        output.console_log("Config.before_experiment() called!")

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""
        ###### Need to kill all other unwanted processes 
        output.console_log("Config.before_run() called!")

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here.
        For example, starting the target system to measure.
        Activities after starting the run should also be performed here."""
        # library = context.run_variation['library']
        # dataframe_size = context.run_variation['dataframe_size']

        ### mapper to call the particular python file by name based on the factors 
        # start the target
        ### mention path cwd = self.ROOT_DIR
        self.target = subprocess.Popen(['python3', 'DAT/Code/DAT/Pandas/Big_Dataset_Size/ViewData.py'],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.ROOT_DIR,
                                       )
        print("hellooooooo I am here", self.target.pid)

        output.console_log("Config.start_run() called!")

    def start_measurement(self, context: RunnerContext) -> None:
        """Perform any activity required for starting measurements."""
        energy_profiler_cmd = f'powerjoular -l -p {self.target.pid} -f {context.run_dir / "powerjoular.csv"}'
        # do we need to make it sleep before measurign as well?
        time.sleep(1) # allow the process to run a little before measuring
        self.energy_profiler = subprocess.Popen(shlex.split(energy_profiler_cmd))

        # check for etimes - doesn't make sense to take mean of it since its not the right value of 
        performance_profiler_cmd = f"ps -p {self.target.pid} --noheader -o '%cpu,%mem,etimes'"
        timer_cmd = f"while true; do {performance_profiler_cmd}; sleep 1; done"
        self.performance_profiler = subprocess.Popen(['sh', '-c', timer_cmd],
                                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE
                                                     )

        output.console_log("Config.start_measurement() called!")

    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""
        self.target.wait()
        output.console_log("Config.interact() called!")

    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""
        os.kill(self.energy_profiler.pid, signal.SIGINT)  # graceful shutdown of powerjoular
        self.energy_profiler.wait()
        self.performance_profiler.kill()
        self.performance_profiler.wait()
        output.console_log("Config.stop_measurement called!")

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run.
        Activities after stopping the run should also be performed here."""
        self.target.kill()
        self.target.wait()
        output.console_log("Config.stop_run() called!")

    def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, SupportsStr]]:
        """Parse and process any measurement data here.
        You can also store the raw measurement data under `context.run_dir`
        Returns a dictionary with keys `self.run_table_model.data_columns` and their values populated"""

        output.console_log("Config.populate_run_data() called!")
        # powerjoular.csv - Power consumption of the whole system
        # powerjoular.csv-PID.csv - Power consumption of that specific process
        df = pd.read_csv(context.run_dir / f"powerjoular.csv-{self.target.pid}.csv")
        psdf = pd.DataFrame(columns=['cpu_usage', 'memory_usage', 'elapsed_time'])
        for i, l in enumerate(self.performance_profiler.stdout.readlines()):
            decoded_line = l.decode('ascii').strip()
            decoded_arr = decoded_line.split()
            cpu_usage = float(decoded_arr[0])
            mem_usage = float(decoded_arr[1])
            elapsed_time = float(decoded_arr[2])
            psdf.loc[i] = [cpu_usage, mem_usage, elapsed_time]
        psdf.to_csv(context.run_dir / 'raw_data.csv', index=False)

        run_data = {
            'ps_avg_cpu': round(psdf['cpu_usage'].mean(), 3),
            'ps_avg_mem': round(psdf['memory_usage'].mean(), 3),
            'avg_elapsed_time': round(psdf['elapsed_time'].mean(), 3),
            'total_energy': round(df['CPU Power'].sum(), 3),
        }
        return run_data

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""

        output.console_log("Config.after_experiment() called!")

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path: Path = None
