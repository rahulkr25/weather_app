# weather_app
                                              Django Backed Weather App

                                   Accessing Weather App deployed on PythonAnywhere

Login API - http://rahulkr25.pythonanywhere.com/login
Either we can register the new user and use the created credentials for login or we can use existing credentials
Username - rahul ;  Password- rahul
After successful authentication it will redirect to home page(http://rahulkr25.pythonanywhere.com/home/), 
From home page two api call can be made to logout from the current session or fetch weather details

Fetch Weather Details API- http://rahulkr25.pythonanywhere.com/get-weather
 This api will redirect to login page if the user hasn’t been authenticated, if the user has already logged in this api will fetch the weather details and will show the weather details of 30 selected cities, with 10 city weather details each page.

Logout API- http://rahulkr25.pythonanywhere.com/logout
After successful logout it will redirect to login page.

                                           Steps for deploying on local host:
1. Clone the source code in local machine:
git clone https://github.com/rahulkr25/weather_app.git
2. Change directory to weather_app
cd weather_app
3. Create a virtual environment
python -m venv vnv
4. Activate the virtual env.
source  vnv/bin/activate
5. Install the requirements.txt file.
pip install -r requirements.txt
6. Change directory to fetchweather
cd fetchweather
7. Make migrations using given two commands.
python manage.py makemigrations
python manage.py migrate
8. Start the server.
python manage.py runserver

Login API- http://127.0.0.1:8000/login/
Get Weather Details API- http://127.0.0.1:8000/get-weather/
Logout API- http://127.0.0.1:8000/logout



