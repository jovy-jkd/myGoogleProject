import csv


def assert_results(output_file):
    # Define thresholds for assertions
    max_response_time_ms = 2000  # Max acceptable response time
    max_error_percentage = 1.0  # Max acceptable error rate

    total_requests = 0
    error_count = 0
    total_response_time = 0
    first_timestamp = None
    last_timestamp = None

    # Process each row in the output CSV file
    with open(output_file, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            total_requests += 1
            response_time = int(row['elapsed'])
            timestamp = int(row['timeStamp'])
            success = row['success'] == 'true'

            # Accumulate metrics
            total_response_time += response_time
            if not success:
                error_count += 1

            # Track the first and last timestamps for duration
            if first_timestamp is None or timestamp < first_timestamp:
                first_timestamp = timestamp
            if last_timestamp is None or timestamp > last_timestamp:
                last_timestamp = timestamp

    # Calculate average response time, error percentage, and throughput
    avg_response_time = total_response_time / total_requests if total_requests else 0
    error_percentage = (error_count / total_requests) * 100 if total_requests else 0
    test_duration_seconds = (last_timestamp - first_timestamp) / 1000 if last_timestamp and first_timestamp else 0
    throughput = total_requests / test_duration_seconds if test_duration_seconds > 0 else 0

    # Assertions based on thresholds
    assert avg_response_time <= max_response_time_ms, f"Average response time exceeded: {avg_response_time} ms"
    assert error_percentage <= max_error_percentage, f"Error rate exceeded: {error_percentage}%"
    print(
        f"Test passed with average response time: {avg_response_time} ms, error rate: {error_percentage}%, and throughput: {throughput} req/sec")

    # Append results summary to the same CSV file
    with open(output_file, mode='a', newline='') as summary_csv:
        writer = csv.writer(summary_csv)
        writer.writerow([])
        writer.writerow(["Summary"])
        writer.writerow(
            ["Total Requests", "Average Response Time (ms)", "Error Percentage (%)", "Throughput (req/sec)"])
        writer.writerow([total_requests, avg_response_time, error_percentage, throughput])

    print(f"Summary appended to {output_file}")

