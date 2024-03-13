import requests

def get_evening_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    evening_temp = data["main"]["temp"]
    return f"Evening temperature in {city}: {evening_temp}°C"

city = "Berlin"  # Example city
print(get_evening_forecast(city))
