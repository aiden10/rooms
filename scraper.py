"""
This url returns JSON of the courses for the subjects included in the query: https://loris.wlu.ca/register/ssb/searchResults/searchResults?txt_subject=73,AB,AF,BH&txt_term=202409&startDatepicker=&endDatepicker=&uniqueSessionId=oz53c1728439597570&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc
This one gets the subjects: https://loris.wlu.ca/register/ssb/classSearch/get_subject?searchTerm=&term=202409&offset=2&max=10&uniqueSessionId=oz53c1728439597570&_=1728440002036
    Increasing the offset will load the next section of courses
So, I just need to get all the subjects, then do a single query which includes all of those subjects to get the JSON containing all the courses
- Get all the room data
- Sample format:
{
    "Rooms": {
        "LH1001": {
            "M": ["08:30 AM - 09:20 AM", ...],
            "T": [],
            "W": [],
            "R": [],
            "F": []
        },
    }
}
Setup some HTML and CSS to display all of this 
Ideal features:
    - View rooms which aren't going to be used for the rest of the day. Can go on a separate page.
    - View all currently available rooms and how long each one will be available for. Can also go on a separate page.
    - Scrollable section for each individual room, and each room can be clicked on to pull up its time table. This can be the homepage.

I think a schedule style table would be good and I can highlight the times the room is occupied in red.

73,AN,AB,AR,AF,AS,BH,BI,BU,MB,BE,CH,CL,CLIM,CS,CP,CC,CQ,KS,DATA,DH,DMJN,EC,EU,EM,EN,ES,FS,FA,FI,FR,DD,GG,GESC,GL,GM,GC,UNDC,GV,GJRC,GS,GR,HE,HS,HI,HN,HR,ID,UU,INED,IP,IT,KP,LL,LA,LY,OL,MGTA,MF,MS,MA,MX,ML,MU,MZ,NO,PP,PC,PD,PO,PS,SAFE,RE,SKRT,SC,SE,61,SK,SOJE,SY,SP,ST,XLAW,TR,TH,UX,WASC,WS,YC
"""
import requests
import json
import os

headers = os.environ.get('headers')
valid_codes = [
    "PS", "SAFE", "RE", "SKRT", "SC", "SE", "61", "SK", "SOJE", "SY", "SP", 
    "ST", "XLAW", "TR", "TH", "UX", "WASC", "WS", "YC"
]
for code in valid_codes:
    url = f'https://loris.wlu.ca/register/ssb/searchResults/searchResults?txt_subject={code}&txt_term=202409&startDatepicker=&endDatepicker=&uniqueSessionId=zi5yx1728450526972&pageOffset=0&pageMaxSize=1000&sortColumn=subjectDescription&sortDirection=asc'
    response = requests.get(url, headers=headers)
    print(response.text)
    json_data = json.loads(response.text)
    if json_data["data"]:
        with open(f"subjects/{code}.json", "w", encoding='utf-8') as file:
            json.dump(json_data, file, indent=4)
        print(f'wrote {code} data to file')
    else:
        print("No data")