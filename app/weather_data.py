"""This module contains the WeatherService class."""
import requests

from decouple import config

from typing import Dict


class WeatherService:
    """Class to get weather data from the OpenWeatherMap API.

    Atributes:
        base_url (str): The base URL for the OpenWeatherMap API.
        api_key (str): The API key for the OpenWeatherMap API.
        params (str): The parameters for the OpenWeatherMap API.
        lang (str): The language for the OpenWeatherMap API.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WeatherService, cls).__new__(cls)
            cls._instance.base_url = config("BASE_URL")
            cls._instance.api_key = config("API_KEY")
            cls._instance.params = config("PARAMS")
            cls._instance.lang = config("LANG")
        return cls._instance

    def get_weather_data(self, city):
        """Get weather data from the OpenWeatherMap API.

        Args:
            city (str): The name of the city to get weather data for.

        Returns:
            dict: A dictionary containing the weather data.
        """
        url = f"{self.base_url}appid={self.api_key}&q={city}&units={self.params}&lang={self.lang}"  # noqa
        response = requests.get(url).json()

        weather_data: Dict[str, str] = {}
        weather_data["temp"]: str = round(response["main"]["temp"])
        weather_data["min_temp"]: str = round(response["main"]["temp_min"])
        weather_data["max_temp"]: str = round(response["main"]["temp_max"])
        weather_data["humidity"]: str = round(response["main"]["humidity"])
        weather_data["pressure"]: str = round(response["main"]["pressure"])
        weather_data["visibility"]: str = round(response["visibility"] / 1000)
        weather_data["wind"]: str = round(response["wind"]["speed"])

        return weather_data
