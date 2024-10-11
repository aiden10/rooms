# Site for viewing Laurier room availability

## About
View rooms which are available and filter by currently empty rooms or rooms which are empty for the rest of the day.

### Data
First I got data from Laurier's course registration site. I initially tried to use their endpoint which returns the data, but I found that it worked somewhat strangely. 
Basically the results that the endpoint returns isn't based on the query but instead based on your last search. I think it probably updates the browser cookies and then the server takes those cookies, verifies them, and then 
returns the response based on that. So I wasn't able to scrape it automatically, but I was able to use one of the endpoints to get all the subject codes and then create a few large searches, and then go to the search results
endpoint and download the JSON.

### Parsing
The next step was to parse all the course JSON data and put it into a more usable format. This is what the ```parser.json``` file is for. It then saves the parsed data into a new JSON file in the schedules directory. 

### Display
Actually displaying the data proved to be the most difficult part. I had initially envisioned a table similar to Lettucemeet but because classes start and end at times like 8:20 or 2:50, I wouldn't be able to make a table
for every hour. I'm sure there are smarter ways to display those times but I ended up going with the most straightforward approach and instead made a row for every ten minutes in a day. Although it's kind of ugly and takes up a lot more
space than I originally wanted.

![rooms1-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/51ba9b08-4258-4f8d-87c8-bb477ac5dd35)
