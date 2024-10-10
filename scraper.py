"""
Buttons on the top of the page to filter and view the rooms which are currently empty and those which are empty for the rest of the day

Finding currently empty rooms:
<div id="currently-empty-rooms"></div>
    var currentDate = new Date();
    var currentTime = new Date(currentDate.getTime());
    var currentlyEmptyRooms = [];
    for (const roomDiv of rooms-container){ // doing it like this so that I can access the divs
        let name = roomDiv.roomName;
        let roomSchedule = rooms[name]; // rooms JSON file might not be accessible and I don't want to pass it around so this might not work
        let valid = isValidTime(roomSchedule, currentTime.hour, currentTime.minute, currentTime.day, currentTime.suffix);
        currentlyEmptyRooms.push(roomDiv);
    }
    rooms-container.style.display = "none"; // hide the original room list
    
    var emptyRoomsDiv = document.getElementById("currently-empty-rooms");
    for (const room in currentlyEmptyRooms){
        emptyRoomsDiv.appendChild(room);
    }

Finding rooms which are empty for the rest of the day:
<div id="empty-rooms"></div>
    var currentDate = new Date();
    var currentTime = new Date(currentDate.getTime());
    var emptyRooms = [];
    var timeCopy = currentTime;
    for (const roomDiv of rooms-container){ // doing it like this so that I can access the divs
        let name = roomDiv.roomName;
        var roomSchedule = rooms[name];
        var roomValid = true;
        while (timeCopy.day === currentTime.day){
            let valid = isValidTime(roomSchedule, timeCopy.hour, timeCopy.minute, timeCopy.day, timeCopy.suffix);
            if (!valid){
                roomValid = false;
                break;
            }
            timeCopy.minute += 10; 
        }
        if (roomValid){
            emptyRooms.push(roomDiv);
        }
        timeCopy = currentTime;
    }
    rooms-container.style.display = "none"; // hide the original room list
    
    var emptyRoomsDiv = document.getElementById("empty-rooms");
    for (const room in emptyRooms){
        emptyRoomsDiv.appendChild(room);
    }

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