import requests
import os

def get_weather_data(city_name):
    API_KEY = "215c86f03be2f93978090ed12ce6a83d"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        rainfall = data.get("rain", {}).get("1h", 0)or 0
        humidity = data["main"]["humidity"]
        temperature = data["main"]["temp"]
        elevation=200

        print(f"City: {city_name}")
        print(f"Rainfall: {rainfall} mm")
        print(f"Humidity: {humidity}%")
        print(f"Temperature: {temperature}°C")

        return [rainfall, humidity, temperature, elevation]
    else:
        print("Error fetching weather data:", data.get("message", "Unknown error"))
        print(response,json())
        return None

