"""
Get winter courses
Add a search bar
Sort alphabetically
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