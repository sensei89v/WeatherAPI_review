
import datetime as dt
from collections import namedtuple

import requests as rq

from api.settings import env


weather_api_token = env('WEATHER_API_TOKEN')

Result = namedtuple('Result', ['success', 'error', 'forecast'])

coordinates = {
    'CZ': '50.073658, 14.418540',  #  Prague
    'SK': '48.148598, 17.107748',  #  Bratislava
    'UK': '51.509865, -0.118092'}  #  London


def get_weather(date, country_code):
    base_url = 'http://api.weatherapi.com/v1/forecast.json'
    url_params = {
        'key': weather_api_token,
        'dt': date,
        'q': coordinates[country_code]}

    try:
        response = rq.get(base_url, params=url_params)
    except rq.ConnectionError:
        return Result(
            False,
            'Network error',
            '')

    if response.status_code == 200:
        temp = response.json()['forecast']['forecastday'][0]['day']['avgtemp_c']
        forecast = weather_status(temp)
        return Result(
            True,
            '',
            forecast)
    else:
        return Result(
            False,
            'Forcast server unavaiable. Try again later',
            '')


def validate_date(request_date):
    today = dt.datetime.now().date()
    max_date = today + dt.timedelta(days=15)
    try:
        date = dt.datetime.strptime(request_date, '%Y-%m-%d').date()
        if date >= today and date <= max_date:
            return Result(
                True,
                '',
                '')
        else:
            return Result(
                False,
                'The date is incorrect',
                '')
    except ValueError:
        return Result(
            False,
            'Date is not acceptable',
            '')
    except:
        return Result(
            False,
            'Unexpected error with a date',
            '')


def validate_country_code(country_code):
    if country_code not in coordinates.keys():
        return Result(
            False,
            'The country code is incorrect',
            '')
    else:
        return Result(
            True,
            '',
            '')


def weather_status(temperature):
    if temperature > 20:
        return 'good'
    elif temperature >= 10:
        return 'soso'
    else:
        return 'bad'
