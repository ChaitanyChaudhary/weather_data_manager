import requests
import json
import csv
import os
from timezone_query import get_time_date

user_location = "chicago"

try:
    # api key is from https://www.weatherapi.com/
    url = f"https://api.weatherapi.com/v1/current.json?key=[YOUR_API_KEY]&q={user_location}"
    
    # api request
    r = requests.get(url)
    wdic = json.loads(r.text)
    wtmp = wdic["current"]["temp_c"]
    wvind = wdic["current"]["wind_mph"]
    cloudy = wdic["current"]["cloud"]
    humidity = wdic["current"]["humidity"]
except Exception as e:
    print(f"API request fails: {e}")


# Get and display the current time and date for the specified location
current_time_date = get_time_date(user_location)

# print weather data into console.
print(f"The current weather in {user_location} is {wtmp} degress \nWind is {wvind} miles per hour \nCloud Cover {cloudy}% \nHumidity {humidity}%")


# For CSV File- 
fields = ['Date&Time', 'Country/State/City', 'Temperature', 'Wind speed', 'Cloudy', 'Humidity']
rows = [ [f'{current_time_date}', f'{user_location}', f'{wtmp} degress', f'{wvind} miles per hour', f'{cloudy}%', f'{humidity}%']]
 
# csv file name
filename = "weather-report.csv"

if not os.path.exists(filename):
    # create/write csv file.
    with open(filename, 'w') as csvfile:
        
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
else:
    # append new data.
    with open(filename, 'a') as csvfile:

        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(fields)
        csvwriter.writerows(rows)

'''
excel shortcut keys- alt+h+o+a
                     alt+h+o+i
'''