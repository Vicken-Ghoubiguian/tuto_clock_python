# import the needed Python modules
import pytz
import datetime
import argparse
import platform
import subprocess
import os
import json
import folium
import sys
import urllib.request
import json

#
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import QUrl

#
try :

     import TimeZoneException as TimeZoneException
     import colors as colors

#
except ImportError:

     #
     from . import TimeZoneException as TimeZoneException
     from . import colors as colors

# from the needed Python modules import needed components
from tzlocal.windows_tz import win_tz

#
def geographical_coordinates_from_timezone(timezone) :
    
    #
    datas = None

    #
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "geographical_coordinates.json")) as gc :

          #
          geographical_coordinates_json = json.load(gc)

    #
    geographical_coordinates = geographical_coordinates_json["geographical_coordinates"]

    #
    for element in geographical_coordinates :

          #
          if timezone in element :

               #
               datas = element[timezone]

               #
               break
     
    #   
    return datas

#
def get_Weather_from_Weather_bit(location, weatherbit_api_key) :

     #
     try :

          #
          weatherUrl = "https://api.weatherbit.io/v2.0/current?lat=" + str(location["latitude"]) + "&lon=" + str(location["longitude"]) + "&key=" + weatherbit_api_key

          #
          with urllib.request.urlopen(weatherUrl) as url:
                    
               #
               weatherDatas = json.loads(url.read().decode())

          #
          print("".join([colors.GREEN,"Weather returned successfully !",colors.END]))
          print("".join([colors.BLUE, "Weather available in the Weather Window !",colors.END]))

          #
          return weatherDatas
     
     #
     except Exception as exception:

          #
          print("".join([colors.RED,"Exception : ",str(exception),colors.END]))

          #
          return None

#
def map_generator_for_location(lat, lon, zoom, tooltip_name, location_name, map_name) :

     #
     try :

          #
          generated_map = folium.Map([lat,lon], zoom_start=zoom)

          #
          folium.Marker(
               location=[lat, lon],
               tooltip=tooltip_name,
               popup=location_name,
               icon=folium.Icon(color="red"),
          ).add_to(generated_map)

          #
          generated_map.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", map_name))

          #
          print("".join([colors.GREEN,"Map generated successfully !",colors.END]))
          print("".join([colors.BLUE,"Map available at ",os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", map_name)),colors.END]))

          #
          return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", map_name))

     #
     except Exception as exception:

          #
          print("".join([colors.RED,"Exception : ",str(exception),colors.END]))

          #
          return None

#
def get_countrycode_of_timezone(wished_timezone):
    
    #
    for countrycode, timezones in pytz.country_timezones.items():
        
        #
        if wished_timezone in timezones:
            
            #
            return countrycode
     
    #
    return None

#
def get_datas_from_particular_countrycode(countrycode) :

     #
     datas = None

     #
     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "countries.json")) as cj :

          #
          countries_json = json.load(cj)

     #
     countries = countries_json["countries"]

     #
     for element in countries :

          #
          if countrycode in element :

               #
               datas = element[countrycode]

               #
               break

     #
     return datas

# Definition of a function to get all timezones
def get_all_timezones():

    # Returning a list of all timezones
    return pytz.all_timezones

# Definition of a function to get all common timezones
def get_all_common_timezones():

     # Returning a list of all common timezones
     return pytz.common_timezones
	
#
def get_datetime_for_particular_timezone(destination_timezone):

    #
    if destination_timezone in pytz.all_timezones :
    
         #
         dtz = pytz.timezone(destination_timezone)
         
         #
         return datetime.datetime.now(dtz)
    
    #
    else :
    
         #
         return None
    
#
def return_iana_timezone() :

    #
    if platform.system() == "Windows" :
    
        #
        return win_tz.get("Romance Standard Time")

    #
    elif platform.system() == "Linux" :
         
         #
         return subprocess.check_output("cat /etc/timezone", shell=True, text=True).replace("\n", "")

    #
    elif platform.system() == "Darwin" :

         #
         return subprocess.check_output("readlink /etc/localtime | sed 's#/var/db/timezone/zoneinfo/##g'", shell=True, text=True).replace("\n", "") 

    #
    else :
         
         #
         return "Etc/UTC"
    
#
if __name__ == "__main__":
    
    #  Get the current timezone of the system
    iana_tz = return_iana_timezone()

    #
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=iana_tz)

    #
    parser.add_argument('--dt_format', action="store", dest='dt_format', default='%Y-%m-%d %H:%M:%S')

    #
    parser.add_argument('--zoom_map', action="store", dest='zoom_map', default=5)
    
    #
    args = parser.parse_args()

    #
    print(get_all_timezones())

    #
    print(get_all_common_timezones())
    
    #
    if get_datetime_for_particular_timezone(args.timezone) != None :
         
         #
         if get_countrycode_of_timezone(args.timezone) != None :

              #
              country = get_datas_from_particular_countrycode(get_countrycode_of_timezone(args.timezone))
              
              #
              unicode_country = country["flag"].encode('utf-8')

              #
              print("".join([args.timezone," (",unicode_country.decode('unicode_escape')," ",country["name"],") : ",get_datetime_for_particular_timezone(args.timezone).strftime(args.dt_format)]))
         #
         else :

              #
              print("".join([args.timezone," : ",get_datetime_for_particular_timezone(args.timezone).strftime(args.dt_format)]))

    #
    else :
         
         #
         raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)
    
    #
    gc = geographical_coordinates_from_timezone(args.timezone)

    #
    if gc is not None :
    
          #
          generated_map = map_generator_for_location(gc["latitude"], gc["longitude"], args.zoom_map, "".join([gc["location"]," location"]), gc["location"], "generated_map_dt_management.html")

          #
          if generated_map is not None :
         
               #
               app = QApplication(sys.argv)

               #
               window = QWebEngineView()

               #
               window.settings().setAttribute(
                    QWebEngineSettings.LocalContentCanAccessRemoteUrls,
                    True
               )

               #
               window.settings().setAttribute(
                    QWebEngineSettings.LocalContentCanAccessFileUrls,
                    True
               )

               #
               window.setWindowTitle("Generated map")

               #
               file_path = os.path.abspath(generated_map)

               #
               window.load(QUrl.fromLocalFile(file_path))

               #
               window.show()

               #
               sys.exit(app.exec())