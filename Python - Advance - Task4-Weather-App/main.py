import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_current_weather(city, unit="metric"):
    """Fetch current weather for a given city"""
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": unit
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


if __name__ == "__main__":
    city = "Phnom Penh"
    weather = get_current_weather(city)
    
    if weather:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Condition: {weather['weather'][0]['description']}")
        print(f"Humidity: {weather['main']['humidity']}%")
    else:
        print("Error fetching weather data")