# Pytest Automation Framework - Performance Testing Using Jmeter, Gatling and Python
-----------------------------------------------------------------------------------------------
This project is an automation framework for to test performance of  googlemap api's using **Jmeter**, **Gatling**, **Python's Pytest and Pymeter** .

- Google Direction, Geolocation and Geocode api's.
- Test execution using PyTest.
- Test using jmeter's jmx file as well as with the web api's directly


**Table of Contents**
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run Tests](#how-to-run-tests)

## **Project Overview**
This framework automates jmeter actions in two ways. 
  - i) The script makes the api calls and assert it
  - ii) Uses the jmx file to make the api calls and then assert it


## **Tech Stack**
- **Python**: Programming language
- **Pymeter**: Python package to capture jmeter tests
- **Pytest**: Test framework for writing and executing test cases
- **Jmeter**: Performance testing tool
- **Gatling**: Performance testing tool

## **Project Structure**
```bash
src
│ 
└── src_utils.py
tests
├── test_direction.py
├── test_direction_jmx.py
├── test_geocode.py
├── test_geocode_jmx.py
├── test_geolocation.py
└── test_geolocation_jmx.py
|output
|reports
│   
└── reports.py
utils
└── logger_utils.py
jmeter-tests
├── GeocodeHTTPRequest.jmx
├── GeolocationHTTPRequest.jmx
├── GoogleDirectionHTTPRequest.jmx
├── MyFirst HTTP Test.jmx
├── ReqResHttpPost.jmx
├── jmeter.log
└── testplan.jmx
```

## **Installation**

### 1. Clone repository
```bash
git clone https://github.com/jovy-jkd/myGoogleProject.git
```
### 2. Install Pymeter
```bash
- pip install pymeter
```
### 3. Install Pytest
```bash
- pip install pytest
- Download jmeter and copy the folder to your projec
```
## **How to Run Tests**
```bash
pytest <test_name>.py
```

