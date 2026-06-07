#
import sys

# import the custom modules as Python modules
import tuto_clock_python.CartographyWindow as CartographyWindow
import tuto_clock_python.dt_management as dt_management
import tuto_clock_python.TimeZoneException as TimeZoneException

# import the QApplication widget from PySide
from PySide6.QtWidgets import QApplication

#  Get the current timezone of the system
iana_tz = dt_management.return_iana_timezone()

#
timezone = input("Entrez une timezone (valeur par défaut: " + iana_tz + ") : ") or iana_tz

#
title = input("Entrez le titre que vous voulez pour afficher la fenêtre (valeur par défaut: 'World's map') : ") or "World's map"

#
dt_format = input("Entrez un format de temps et de date (valeur par défaut: %Y-%m-%d %H:%M:%S) : ") or " %Y-%m-%d %H:%M:%S"

#
zoom_map = input("Entrez la valeur du zoom sur la carte (valeur par défaut: 5) : ") or "5"

#
width = input("Entrez la largeur de la fenêtre (valeur par défaut: 1200) : ") or "1200"

#
height = input("Entrez la hauteur de la fenêtre (valeur par défaut: 800) : ") or "800"

#
if dt_management.get_datetime_for_particular_timezone(timezone) != None :
         
    #
    if dt_management.get_countrycode_of_timezone(timezone) != None :

        #
        country = dt_management.get_datas_from_particular_countrycode(dt_management.get_countrycode_of_timezone(timezone))
              
        #
        unicode_country = country["flag"].encode('utf-8')

        #
        print("".join([timezone," (",unicode_country.decode('unicode_escape')," ",country["name"],") : ",dt_management.get_datetime_for_particular_timezone(timezone).strftime(dt_format)]))
    #
    else :

        #
        print("".join([timezone," : ",dt_management.get_datetime_for_particular_timezone(timezone).strftime(dt_format)]))

#
else :
         
    #
    raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)
    
#
gc = dt_management.geographical_coordinates_from_timezone(timezone)

#
if gc is not None :

    #
    app = QApplication(sys.argv)
    
    #
    viewMap = CartographyWindow.CartographyWindow(timezone, title, int(zoom_map), int(width), int(height), "generated_map_test_2.html")
         
    #
    viewMap.start()

    #
    sys.exit(app.exec())