import requests

from decouple import config


class WeatherService:
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
        url = f"{self.base_url}appid={self.api_key}&q={city}&units={self.params}&lang={self.lang}"  # noqa
        response = requests.get(url).json()

        weather_data = {}
        weather_data["temp"] = round(response["main"]["temp"])
        weather_data["min_temp"] = round(response["main"]["temp_min"])
        weather_data["max_temp"] = round(response["main"]["temp_max"])
        weather_data["humidity"] = round(response["main"]["humidity"])
        weather_data["pressure"] = round(response["main"]["pressure"])
        weather_data["visibility"] = round(response["visibility"] / 1000)
        weather_data["wind"] = round(response["wind"]["speed"])

        return weather_data
