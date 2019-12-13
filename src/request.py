#Function: this is a python script that checks to see if coverage reported from the Codecov API is accurate

import requests
import time
import os

payload = {'token': os.environ['CODECOV_API_KEY']}

link = 'https://codecov.io/api/gh/codecov/Python-Standard'

print("Waiting 60 seconds for report to upload before pinging API...")

#night night
time.sleep(60)

print("Pinging Codecov's API..")
#get latest coverage data
all_data = requests.get(link, params=payload).json()
commit_data = all_data['commits'][0]
coverage_percentage = commit_data['totals']['c']

print("Ensuring coverage percentage is accurate...")
#result should return 85.71429 as its coverage metric
CORRECT_COVERAGE = "85.71429"
print("COVERAGE VALUES")
print("Expected: " + CORRECT_COVERAGE + "%, Actual: " + coverage_percentage + "%")

if(coverage_percentage == CORRECT_COVERAGE): 
    print("SUCCESS. Codecov API returned correct coverage percentage.")
    exit(0)
else:
	print("FAILURE. Codecov API did not return correct coverage percentage.")
    exit(1)
