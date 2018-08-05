from django.shortcuts import render
import requests
from .models import City, check_crop
from .forms import CityForm
import datetime

def index(request):
    cities = City.objects.all() #return all the cities in the database

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context) #returns the index.html template

def data(request):
    crops = check_crop.objects.all()
    time = []
    now = datetime.datetime.today()
    time.append(now.strftime("%Y-%m-%d"))
    for i in range(4):
        now += datetime.timedelta(days=1)
        time.append(now.strftime("%Y-%m-%d"))

    if request.method == 'GET':
        city = request.GET.get('q')

        url = 'http://api.openweathermap.org/data/2.5/forecast?q={},in&appid=271d1234d3f497eed5b1d80a07b3fcd1&units=metric'

        weather_data = []

        city_weather = requests.get(url.format(city)).json()

        if request.method == 'GET':
            crp = request.GET.get('crp')
        print(crp)

        for i in range(0, 40, 8):
            weather = {
                'city' : city,
                'temperature' : city_weather['list'][i]['main']['temp'],
                'description' : city_weather['list'][i]['weather'][0]['description'],
                'icon' : city_weather['list'][i]['weather'][0]['icon']
            }
            weather_data.append(weather)


        context = {'weather_data' : weather_data, 'crops' : crops, 'time' : time, 'crp' : crp}
    return render(request, 'weather/data.html', context)
