import json
import os
schedule = {"Rooms": {}}
for file in os.listdir("winter_courses"):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        fn = os.path.join("winter_courses", filename)
        with open(fn, "r") as courses_file:
            course_data = json.load(courses_file)["data"]
            for course in course_data:
                term = course["termDesc"]
                subject = course["subjectDescription"]
                campus = course["campusDescription"]
                meeting_info = course["meetingsFaculty"]
                if len(meeting_info) > 0:
                    meeting_info = meeting_info[0]
                    meeting_time = meeting_info["meetingTime"]
                    class_start_time = meeting_time["beginTime"]
                    if class_start_time:
                        class_start_time = class_start_time[:2] + ":" + class_start_time[2:]
                    class_end_time = meeting_time["endTime"]
                    if class_end_time:
                        class_end_time = class_end_time[:2] + ":" + class_end_time[2:]

                    building = meeting_time["buildingDescription"]
                    if building == 'MartinLuther UniversityCollege': building = 'Martin Luther University College'
                    room = meeting_time["room"]
                    monday = meeting_time["monday"]
                    tuesday = meeting_time["tuesday"]
                    wednesday = meeting_time["wednesday"]
                    thursday = meeting_time["thursday"]
                    friday = meeting_time["friday"]

                if building and room and building != 'VIRTUAL' and 'Brant' not in campus and 'Milton' not in building and 'Kitchener' not in building:
                    location = f'{building} {room}'
                    if location not in schedule["Rooms"]:
                        schedule["Rooms"].update({location: {"M": [],"T": [],"W": [],"R": [],"F": []}})
                    if monday: schedule["Rooms"][location]["M"].append((class_start_time, class_end_time))
                    if tuesday: schedule["Rooms"][location]["T"].append((class_start_time, class_end_time))
                    if wednesday: schedule["Rooms"][location]["W"].append((class_start_time, class_end_time))
                    if thursday: schedule["Rooms"][location]["R"].append((class_start_time, class_end_time))
                    if friday: schedule["Rooms"][location]["F"].append((class_start_time, class_end_time))

with open("schedules/winter.json", "w") as file:
    json.dump(schedule, file)