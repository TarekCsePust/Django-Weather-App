from django.shortcuts import render,HttpResponse
import requests
from .forms import CityForm
from .models import City
# Create your views here.

def index(request):
    city = "Mumbai"
   
    #apiCall = 'https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={APP ID}'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        app = 'https://api.openweathermap.org/data/2.5/weather?q=' + city.name + '&appid={APP ID}';
        r = requests.get(app.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)