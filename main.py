from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from weather_data import WeatherService

app = Flask(__name__)

weather_service = WeatherService()


@app.route("/", methods=["GET", "POST"])
def index():
    ciudades = [
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

    datos_ciudades = {}

    for ciudad in ciudades:
        datos_ciudades[ciudad] = weather_service.get_weather_data(ciudad)

    if request.method == "POST":
        try:
            city = request.form["city"]
            weather_data = weather_service.get_weather_data(city)

            return render_template(
                "index.html", city=city, **weather_data, ciudades=datos_ciudades
            )
        except KeyError:
            return redirect(url_for("index"))

    return render_template("index.html", ciudades=datos_ciudades)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
