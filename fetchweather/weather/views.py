import requests

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.cache import cache
from .models import Weather


@login_required(login_url="login")
def HomePage(request):
    return render(request, "home.html")


def SignupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email_id = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return HttpResponse("Passwords didn't Match!")
        else:
            my_user = User.objects.create_user(username, email_id, password1)
            my_user.save()
            return redirect("login")

    return render(request, "signup.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def get_weather(request):

    caching_enabled = cache.get("is_cache_enabled")
    if caching_enabled is None:

        cities = ["Abu Dhabi", "Ahmedabad", "Amsterdam", "Athens", "Auckland", "Bangkok", "Barcelona", "Beijing", "Beirut", "Bengaluru",
        "Berlin", "Brisbane", "Brussels", "Budapest", "Buenos Aires", "Busan", "Cairo", "Canberra", "Cape Town", "Casablanca", 
        "Chennai", "Chicago", "Colombo", "Copenhagen", "Dallas", "Delhi", "Denver", "Dhaka", "Doha", "Dubai"]
        
        api_key = "5ec11febc38413ca3a46b9e14c10bbc0"
        weather_data = []

        for city in cities:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(
                city, api_key
            )
            response = requests.get(url)
            weather_data.append(response.json())

        # Save weather data to database
        Weather.objects.all().delete()  # Remove existing weather data from database
        for data in weather_data:
            try:
                city = data["name"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                weather_description = data["weather"][0]["description"]

                weather = Weather(
                    city=city,
                    temperature=temperature,
                    humidity=humidity,
                    weather_description=weather_description,
                )
                weather.save()
            except:
                 #print('Data Not available for certain cities])
                 pass
        cache.set("is_cache_enabled", True, (60*30))

    # Retrieve weather data from database and paginate
    weather_data = Weather.objects.all()
    paginator = Paginator(
        weather_data, 10
    )  # You can update the number of items per page here
    page = request.GET.get("page")
    weather_data = paginator.get_page(page)

    return render(request, "weather.html", {"weather_data": weather_data})
