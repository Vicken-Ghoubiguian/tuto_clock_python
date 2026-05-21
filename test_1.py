# import the custom modules as Python modules
import tuto_clock_python.Clock as Clock
import tuto_clock_python.dt_management as dt_management

# import the custom exceptions as Python modules
import tuto_clock_python.TimeZoneException as TimeZoneException


#  Get the current timezone of the system
iana_tz = dt_management.return_iana_timezone()

#
timezone = input("Entrez une timezone (ex: " + iana_tz + ") : ") or iana_tz

#
dt_format = input("Entrez un format de temps et de date (ex: %Y-%m-%d %H:%M:%S) : ") or " %Y-%m-%d %H:%M:%S"

#
zoom_map = input("Entrez la valeur du zoom sur la carte (ex: 5) : ") or "5"

#
width = input("Entrez la largeur de la fenêtre (ex: 1500) : ") or "1500"

#
height = input("Entrez la hauteur de la fenêtre (ex: 500) : ") or "500"

#
title = input("Entrez le titre que vous voulez pour afficher la fenêtre (ex: 'Clock') : ") or "Clock"

#
if dt_management.get_datetime_for_particular_timezone(timezone) != None :

    #
    clock = Clock.Clock(timezone, dt_format, int(zoom_map), title, int(width), int(height))

#
else :
         
    #
    raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

#
clock.run()

