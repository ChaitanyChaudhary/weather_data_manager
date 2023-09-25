import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

def get_time_date(location_name):
    try:
        # Use geopy to get the latitude and longitude of the given location
        geolocator = Nominatim(user_agent="time_zone_locator")
        location = geolocator.geocode(location_name)

        if location:
            # Use TimezoneFinder to get the timezone for the coordinates
            tf = TimezoneFinder()
            city_timezone = tf.timezone_at(lng=location.longitude, lat=location.latitude)

            if city_timezone:
                # Get the current time in the specified city
                city_time = datetime.datetime.now(datetime.timezone.utc).astimezone(pytz.timezone(city_timezone))

                # Format the time and date
                formatted_time_date = city_time.strftime("%d %b %Y %H:%M:%S")
                return formatted_time_date
            else:
                return "Timezone not found for the given location."
        else:
            return "Location not found."

    except Exception as e:
        return f"An error occurred: {str(e)}"
