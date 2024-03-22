import openmeteo_requests
import requests_cache
import numpy as np
import pandas as pd
from retry_requests import retry


# Setup the Open-Meteo API client with cache and retry on error
def load_data(_start, _end, _city):
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": [47.36, 46, 47.26, 46.5],
        "longitude": [8.55, 8.95, 11.39, 11.35],
        "start_date": _start,
        "end_date": _end,
        "hourly": ["temperature_2m", "surface_pressure", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"]
    }
    data = openmeteo.weather_api(url, params=params)
    # Process daily data. The order of variables needs to be the same as requested.
    responses = openmeteo.weather_api(url, params=params)
    data_list = []
    if _city == "Zurich":
        city_query = [0, 1]
        print(city_query)
        for _city in city_query:
            response = responses[_city] #append function to an empty list
            hourly = response.Hourly()
            _start = pd.to_datetime(hourly.Time(), unit = "s", utc = True)
            _end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True)
            _delta = pd.Timedelta(seconds = hourly.Interval())

            data = {
                "date": pd.date_range(_start, _end, freq=_delta, inclusive="left"),
                "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
                "surface_pressure": hourly.Variables(1).ValuesAsNumpy(),
                "wind_speed_10m": hourly.Variables(2).ValuesAsNumpy(),
                "wind_direction_10m": hourly.Variables(3).ValuesAsNumpy(),
                "wind_gusts_10m": hourly.Variables(4).ValuesAsNumpy(),
            }
            data_list.append(pd.DataFrame(data).set_index("date"))
    elif _city == "Innsbruck":
        city_query = [2, 3]
        print(city_query)
        for _city in city_query:
            response = responses[_city] #append function to an empty list
            hourly = response.Hourly()
            _start = pd.to_datetime(hourly.Time(), unit = "s", utc = True)
            _end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True)
            _delta = pd.Timedelta(seconds = hourly.Interval())

            data = {
                "date": pd.date_range(_start, _end, freq=_delta, inclusive="left"),
                "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
                "surface_pressure": hourly.Variables(1).ValuesAsNumpy(),
                "wind_speed_10m": hourly.Variables(2).ValuesAsNumpy(),
                "wind_direction_10m": hourly.Variables(3).ValuesAsNumpy(),
                "wind_gusts_10m": hourly.Variables(4).ValuesAsNumpy(),
            }
            data_list.append(pd.DataFrame(data).set_index("date"))
    data_combined = pd.concat(data_list, axis=1)
    return data_combined
# Example
if __name__=="__main__":
    data_new = load_data("2024-02-10", "2024-03-15", "Zurich")
    print(data_new)



""" # Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": [47.36, 46, 47.26, 46.5],
	"longitude": [8.55, 8.95, 11.39, 11.35],
	"start_date": "2024-02-10",
	"end_date": "2024-03-15",
	"hourly": ["temperature_2m", "surface_pressure", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"]
}
original_data = openmeteo.weather_api(url, params=params)
data = dict(zip(("Zurich", "Lugano", "Innsbruck", "Bolzano"), original_data))
data = pd.concat({key: make_dataframe(val) for key, val in data.items()})

city_codes = {"Zurich": 1, "Lugano": 2, "Innsbruck": 3, "Bolzano": 4}
data['city_code'] = data.index.get_level_values(0).map(city_codes)

original_data = dict(zip(("Zurich", "Lugano", "Innsbruck", "Bolzano"), original_data))
original_data = pd.concat({key: make_dataframe(val) for key, val in original_data.items()})

"""
