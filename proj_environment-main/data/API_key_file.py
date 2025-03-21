import requests
import json

# Define API key and location
API_KEY = "47be05cb17d1568be2c80e4f81e1e1cb"  # Replace with your actual API key
LAT = 59.91  # Latitude for Oslo
LON = 10.75  # Longitude for Oslo

# API endpoint
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

# Make API request
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    
    # Save JSON to a file
    with open("weather_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("Weather data saved to weather_data.json")
else:
    print(f"Error: {response.status_code}, {response.text}")
