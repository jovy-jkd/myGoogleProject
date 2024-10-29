

report_output_folder = "../output"
jmeter_exe_path = "../apache-jmeter-5.6.3/bin/jmeter"
number_of_threads1 = 10
thread_iterations1 = 1
geocode_http_request_jmx_location = "../jmeter-tests/GeocodeHTTPRequest.jmx"
direction_http_request_jmx_location = "../jmeter-tests/GoogleDirectionHTTPRequest.jmx"
geolocation_http_post_jmx_location = "../jmeter-tests/GeolocationHTTPRequest.jmx"
geolocation_post_payload = { "homeMobileCountryCode":310,
   "homeMobileNetworkCode":410,
   "radioType":"gsm",
   "carrier":"Vodafone",
   "considerIp":True
}
report_output_folder_path = report_output_folder + "/"
output_pdf_path = "../reports/"
selected_timestamp = 'timeStamp'
selected_elapsed = 'elapsed'
selected_latency = 'Latency'
selected_throughput = 'Throughput'

