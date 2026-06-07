#
import sys

# import the custom modules as Python modules
import tuto_clock_python.WeatherWindow as WeatherWindow
import tuto_clock_python.dt_management as dt_management
import tuto_clock_python.TimeZoneException as TimeZoneException
import tuto_clock_python.WeatherAPIException as WeatherAPIException

# import the QApplication widget from PySide
from PySide6.QtWidgets import QApplication

#  Get the current timezone of the system
iana_tz = dt_management.return_iana_timezone()

#
timezone = input("Entrez une timezone (valeur par défaut: " + iana_tz + ") : ") or iana_tz

#
width = input("Entrez la largeur de la fenêtre (valeur par défaut: 1500) : ") or "1500"

#
height = input("Entrez la hauteur de la fenêtre (valeur par défaut: 500) : ") or "500"

#
title = input("Entrez le titre que vous voulez pour afficher la fenêtre (valeur par défaut: 'Weather') : ") or "Weather"

#
weatherbit_api_key = input("Entrez la clé API de Weatherbit (valeur par défaut: '') : ") or ""

#
if dt_management.get_datetime_for_particular_timezone(timezone) != None :

     #
    app = QApplication(sys.argv)

    #
    weather_window = WeatherWindow.WeatherWindow(timezone, title, int(width), int(height), weatherbit_api_key)

    #
    weather_window.show()

    #
    sys.exit(app.exec())

#
else :

    #
    raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)