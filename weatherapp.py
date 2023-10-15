import requests
import datetime as dt
from geopy.geocoders import Nominatim

print("Welcome to the Weather App!!\n",end="")

APIkey="189cc4be21b68b09731e83519bdafed6"
while True:
    try:
        city= input("Name of the Location: ")

        loc = Nominatim(user_agent="getlocation")
        getLoc = loc.geocode(city)
        url=f"https://api.openweathermap.org/data/2.5/weather?lat={getLoc.latitude}&lon={getLoc.longitude}&appid={APIkey}"
        break
    except Exception:
        print("Please enter a valid city name\n")

#response is a dictionary
response=requests.get(url).json()
print(f"\n*Current Weather Report of {city}*\n")
def kelvin_to_celsius(t):
    return f"{round(t-273.15,2)}°C", f"{round(((t-273.15)*(9/5))+32,2)}°F"
print(f"Temperature: {kelvin_to_celsius(response['main']['temp'])[0]} ({kelvin_to_celsius(response['main']['temp'])[1]})")
print(f"Humidity: {response['main']['humidity']}%")
print(f"Feels like: {kelvin_to_celsius(response['main']['feels_like'])[0]} ({kelvin_to_celsius(response['main']['feels_like'])[1]})")

print("General Weather: ",response['weather'][0]['description'])
print("Sunrise Time: ",dt.datetime.fromtimestamp(response['sys']['sunrise']).strftime('%H:%M'),"IST", "\nSunset Time: ",dt.datetime.fromtimestamp(response['sys']['sunset']).strftime('%H:%M'),"IST")

name=response['name']
print(f"\nData has been fetched from the Location: {name}, ({getLoc.address})")