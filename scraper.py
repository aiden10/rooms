"""
Setup some HTML and CSS to display all of this 
Ideal features:
    - View rooms which aren't going to be used for the rest of the day. Can go on a separate page.
    - View all currently available rooms and how long each one will be available for. Can also go on a separate page.
    - Scrollable section for each individual room, and each room can be clicked on to pull up its time table. This can be the homepage.

I think a schedule style table would be good and I can highlight the times the room is occupied in red.
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