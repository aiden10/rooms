# Site for viewing Laurier room availability

# Note
Not all of the rooms are classrooms. Some may be labs or other specialized rooms. Also even if there are no classes there may still be people in the room for other reasons. If you want to ensure that a room is empty, you can check the club [events page](https://laurierstudentsunion.presence.io/events). Rooms are typically not listed on there, but the club's Instagram page will usually have it.

## About
View rooms which are available and filter by currently empty rooms, or rooms which are empty for the rest of the day.

### Data
First I got data from Laurier's course registration site and used one of the endpoints to download the course information. The next step was to parse all the course JSON data and put it into a more usable format. This is what the ```parser.json``` file is for. It then saves the parsed data into a new JSON file in the schedules directory. 
   
![rooms1-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/51ba9b08-4258-4f8d-87c8-bb477ac5dd35)
