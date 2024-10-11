"""
Get winter courses
Add a search bar
Improve the initial load time
    The valid times really only need to be calculated once
    
73,AN,AB,AR,AF,AS,BH,BI,BU,MB,BE,CH,CL,CLIM,CS,CP,CC,CQ,KS,DATA,DH,DMJN,EC,EU,EM,EN,ES,FS,FA,FI,FR,DD,GG,GESC,GL,GM,GC,UNDC,GV,GJRC,GS,GR,HE,HS,HI,HN,HR,ID,UU,INED,IP,IT,KP,LL,LA,LY,OL,MGTA,MF,MS,MA,MX,ML,MU,MZ,NO,PP,PC,PD,PO,PS,SAFE,RE,SKRT,SC,SE,61,SK,SOJE,SY,SP,ST,XLAW,TR,TH,UX,WASC,WS,YC
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