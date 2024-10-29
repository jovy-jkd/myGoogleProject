import os
from datetime import datetime
from pymeter.api import ContentType
from pymeter.api.config import ThreadGroupSimple, TestPlan
from pymeter.api.reporters import HtmlReporter
from pymeter.api.samplers import HttpSampler
from src.src_utils import *


def test_geolocation():
    # Define the URL and payload for the POST request
    post_url = google_geolocation_post_api
    post_payload = geolocation_post_payload

    # Create HTTP sampler for POST request with a body
    http_sampler = (HttpSampler("echo_post_request", post_url)
                    .post(post_payload, ContentType.APPLICATION_JSON)
                    )

    # Create a thread group with 10 threads for 1 iteration and add the HTTP sampler
    thread_group = ThreadGroupSimple(number_of_threads1, thread_iterations1, http_sampler)

    # Set up output folder and reporter
    output_dir = os.path.join(report_output_folder, f"perftest_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log")
    html_reporter = HtmlReporter(output_dir)

    # Create a test plan with the thread group and reporter
    test_plan = TestPlan(thread_group, html_reporter)

    # Run the test plan and gather results
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

    # Assert that the 99th percentile of response time is less than 2000 milliseconds
    assert (
        stats.sample_time_99_percentile_milliseconds <= 2000
    ), f"99th percentile should be less than 2000 milliseconds, got {stats.sample_time_99_percentile_milliseconds}"
