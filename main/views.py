from django.shortcuts import render
import json
import urllib.request
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def home(request):
    
    if request.method == "POST":
        
        city = request.POST['city'].replace(" ", "")
        
        try:
            # Get current weather data
            current_source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + os.getenv('API_KEY')).read()
            current_data = json.loads(current_source)
            
            # Check if the response code indicates a successful request
            if current_data['cod'] == 200:
                # Get 5-day forecast data
                forecast_source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=' + city + os.getenv('API_KEY')).read()
                forecast_data = json.loads(forecast_source)
                
                # Extract relevant forecast information
                forecast_dict = {}
                for entry in forecast_data['list']:
                    timestamp = entry['dt']
                    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                    
                    if date not in forecast_dict:
                        forecast_dict[date] = []
                    
                    forecast_dict[date].append({
                        'timestamp': timestamp,
                        'date': datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                        "time": datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M'),
                        'temp': round(entry['main']['temp'] - 273.15, 2),
                        'wind_speed': entry['wind']['speed'],
                        'humidity': entry['main']['humidity'],
                        'weather_description': entry['weather'][0]['description'],
                        'weather_icon': entry['weather'][0]['icon'],
                    })
                
                data = {
                    "city_name": current_data['name'],
                    "date": datetime.datetime.now(),
                    "temp": round(current_data['main']['temp'] - 273.15, 2),
                    "wind_speed": current_data['wind']['speed'],
                    "humidity": current_data['main']['humidity'],
                    "weather_description": current_data['weather'][0]['description'],
                    "weather_icon": current_data['weather'][0]['icon'],
                    "lon": current_data['coord']['lon'],
                    "lat": current_data['coord']['lat'],
                    "feels_like": round(current_data['main']['feels_like'] - 273.15, 2),
                    "temp_min": round(current_data['main']['temp_min'] - 273.15, 2),
                    "temp_max": round(current_data['main']['temp_max'] - 273.15, 2),
                    "pressure": current_data['main']['pressure'],
                    "visibility": current_data['visibility'],
                    "forecast": forecast_dict,
                }
            else:
                # Handle the case where the city does not exist
                error_message = f"City '{city}' not found. Please enter a valid city name."
                return render(request, "main/error.html", context={'error_message': error_message})
            
        except urllib.error.HTTPError as e:
            # Handle other HTTP errors, e.g., 404 Not Found
            error_message = f"Error: {e.code} - {e.reason}"
            return render(request, "main/error.html", context={'error_message': error_message})
        
    else:
        data = {}
        
    return render(request, "main/index.html", context={'data': data})
