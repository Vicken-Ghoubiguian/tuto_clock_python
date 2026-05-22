# import the custom modules as Python modules
import tuto_clock_python.Clock as Clock
import tuto_clock_python.dt_management as dt_management

# import the custom exceptions as Python modules
import tuto_clock_python.TimeZoneException as TimeZoneException


#  Get the current timezone of the system
iana_tz = dt_management.return_iana_timezone()

#
timezone = input("Entrez une timezone (valeur par défaut: " + iana_tz + ") : ") or iana_tz

#
dt_format = input("Entrez un format de temps et de date (valeur par défaut: %Y-%m-%d %H:%M:%S) : ") or " %Y-%m-%d %H:%M:%S"

#
zoom_map = input("Entrez la valeur du zoom sur la carte (valeur par défaut: 5) : ") or "5"

#
width = input("Entrez la largeur de la fenêtre (valeur par défaut: 1500) : ") or "1500"

#
height = input("Entrez la hauteur de la fenêtre (valeur par défaut: 500) : ") or "500"

#
title = input("Entrez le titre que vous voulez pour afficher la fenêtre (valeur par défaut: 'Clock') : ") or "Clock"

#
weatherbit_api_key = input("Entrez la clé API de Weatherbit (valeur par défaut: '') : ") or ""

#
if dt_management.get_datetime_for_particular_timezone(timezone) != None :

    #
    clock = Clock.Clock(timezone, dt_format, int(zoom_map), title, int(width), int(height), weatherbit_api_key)

#
else :
         
    #
    raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

#
clock.run()

