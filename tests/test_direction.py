import os
from datetime import datetime
from pymeter.api.config import TestPlan, ThreadGroupSimple, ThreadGroupWithRampUpAndHold, SetupThreadGroup, \
    TeardownThreadGroup, CsvDataset
from pymeter.api.reporters import HtmlReporter
from pymeter.api.samplers import HttpSampler, DummySampler
from src.src_utils import *


def test_direction():
    # create HTTP sampler, sends a get request to the given url
    http_sampler = HttpSampler("echo_get_request", google_direction_get_api)

    # create a thread group with 10 threads that runs for 1 iterations, give it the http sampler as a child input
    thread_group = ThreadGroupSimple(number_of_threads1, thread_iterations1, http_sampler)

    # puts the report in to the output folder with distinct names
    output_dir = os.path.join(report_output_folder_path, f"perftest_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
    html_reporter = HtmlReporter(output_dir)

    # create a test plan with the required thread group
    test_plan = TestPlan(thread_group, html_reporter)

    # run the test plan and take the results
    stats = test_plan.run()
    print(
                f"duration= {stats.duration_milliseconds}",
                f"mean= {stats.sample_time_mean_milliseconds}",
                f"min= {stats.sample_time_min_milliseconds}",
                f"median= {stats.sample_time_median_milliseconds}",
                f"90p= {stats.sample_time_90_percentile_milliseconds}",
                f"95p= {stats.sample_time_95_percentile_milliseconds}",
                f"99p= {stats.sample_time_99_percentile_milliseconds}",
                f"max= {stats.sample_time_max_milliseconds}",
                sep="\t",
            )

    # Assert that the 99th percentile of response time is less than 2000 milliseconds.
    assert (
        stats.sample_time_99_percentile_milliseconds <= 2000
    ), f"99th percentile should be less than 2000 milliseconds, got {stats.sample_time_99_percentile_milliseconds}"