import csv
import os
import subprocess
import uuid
from datetime import datetime
from reports.reports import Reports
import pymeter
from pymeter.api.config import TestPlan, ThreadGroupSimple
from pymeter.api.reporters import HtmlReporter

from src.assert_results import assert_results
from src.src_utils import *


def test_direction_jmx():
    # path to your jmeter executable
    jmeter_path = os.path.join(jmeter_exe_path)
    # Path to your JMX test plan
    jmx_file = os.path.join(direction_http_request_jmx_location)
    # Path to the output results file (csv format)
    file_name = f"jmxtest_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.csv"
    output_file = os.path.join(report_output_folder, file_name)
    command = [
        jmeter_path,
        "-n",  # Non-GUI mode
        "-t", jmx_file,  # Test plan file
        "-l", output_file]  # Output results file

    # Execute the command
    stats = subprocess.run(command, check=True)
    assert_results(output_file)
    rt = Reports(file_name)
    rt.gen_reports()


# Run the test function
test_direction_jmx()
