"""
Make each roomDiv collapsible
scheduleDiv contains:
    Create a table similar to what lettucemeet has. This will expand/collapse when clicking on the roomDiv.
    Available times are white, occupied times are red
    Table rows are divided into 10 minute sections, but the lines will only show every hour
    Table columns are divided by day (Monday, Tuesday, Wednesday...)

    5 columns
    24 visible rows (one for each hour)
    1440 actual rows 

Buttons on the top of the page to filter and view the rooms which are currently empty and those which are empty for the rest of the day

"""
import requests
import json
import os

headers = os.environ.get("headers")
valid_codes = []
with open("codes.json") as subject_file:
    subjects = json.load(subject_file)
    for subject in subjects["subjects"]:
        code = subject["code"]
        description = subject["description"]
        if 'UW-' not in description: 
            valid_codes.append(code)
print(valid_codes)
for code in valid_codes:
    url = f'https://loris.wlu.ca/register/ssb/searchResults/searchResults?txt_subject={code}&txt_term=202409&startDatepicker=&endDatepicker=&uniqueSessionId=zi5yx1728450526972&pageOffset=0&pageMaxSize=1000&sortColumn=subjectDescription&sortDirection=asc'
    response = requests.get(url, headers=headers)
    print(response.text)
    json_data = json.loads(response.text)
    if json_data["data"]:
        with open(f"courses/{code}.json", "w", encoding='utf-8') as file:
            json.dump(json_data, file, indent=4)
        print(f'wrote {code} data to file')
    else:
        print("No data")