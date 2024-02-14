"""This module contains the views of the application."""
from flask import url_for
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from app.weather_data import WeatherService

from typing import List, Dict


index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)

weather_service = WeatherService()


@index_bp.route("/", methods=["GET", "POST"])
def index():
    """Index view.

    Returns:
        The index.html template.
    """
    ciudades: List[str] = [
        "Tokio",
        "Seúl",
        "Delhi",
        "Bombai",
        "Sao Paulo",
        "Mexico City",
        "Nueva York",
        "Jakarta",
        "Shangai",
    ]

    datos_ciudades: Dict[str, str] = {}

    for ciudad in ciudades:
        datos_ciudades[ciudad]: str = weather_service.get_weather_data(ciudad)

    if request.method == "POST":
        try:
            city = request.form["city"]
            weather_data = weather_service.get_weather_data(city)

            return render_template(
                "index.html",
                city=city,
                **weather_data,
                ciudades=datos_ciudades
            )
        except KeyError:
            return redirect(url_for("index"))

    return render_template("index.html", ciudades=datos_ciudades)
