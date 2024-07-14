from django.shortcuts import render
import requests
import datetime

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'a0314fcea976bb9f7003bd563c635413'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric'

        response = requests.get(url)

        weather_data = response.json()

        if weather_data.get('cod') == 200:
            dt = datetime.datetime.fromtimestamp(weather_data['dt'])
            formatted_datetime = dt.strftime("%d %B %Y %H:%M:%S")

            context = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'datetime': formatted_datetime
            }
        else:
            context = {
                'error': 'City not found!'
            }
        
        return render(request, 'weather/index.html', context)

    return render(request, 'weather/index.html')
