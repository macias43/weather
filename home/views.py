from django.shortcuts import render
import requests

def home(request):
    city = request.GET.get('city', 'New York')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9d69ebde5d7b886a4c8df538f7d40dd0'
    data = requests.get(url).json()

    try:
        payload = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'fahrenheit_temperature': round((data['main']['temp'] * 1.8) - 459.67),
            'celsius_temperature': int(data['main']['temp'] - 273),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['main'],
        }
    except KeyError:
        # Handle the KeyError here, e.g., by setting default values or displaying an error message.
        payload = {
            'city': 'City not found',
            'weather': 'N/A',
            'icon': 'N/A',
            'fahrenheit_temperature': 'N/A',
            'celsius_temperature': 'N/A',
            'pressure': 'N/A',
            'humidity': 'N/A',
            'description': 'N/A',
        }

    context = {'data': payload}
    return render(request, 'home.html', context)
