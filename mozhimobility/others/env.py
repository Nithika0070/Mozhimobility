import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def calculate_environmental_impact(weather_data):
    # Your environmental impact calculation logic here
    # For simplicity, let's assume a basic impact score based on temperature
    temperature = weather_data["main"]["temp"]
    if temperature > 25:
        return "High environmental impact reduce CO2 emission"
    elif 15 <= temperature <= 25:
        return "Moderate environmental impact "
    else:
        return "Low environmental impact"

def main():
    api_key = "648956d73a40b7e9d8b6e26e21b9d6b5"
    city = "Navalur"

    weather_data = get_weather_data(api_key, city)

    if weather_data:
        environmental_impact = calculate_environmental_impact(weather_data)
        print(f"Environmental Impact in {city}: {environmental_impact}")
    else:
        print("Unable to fetch weather data.")

if _name_ == "_main_":
    main()