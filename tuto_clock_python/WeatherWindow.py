# import the needed Python modules
import sys
import os
import requests

#
try :

    #
    import dt_management as dt_management

    # import the custom exceptions as Python modules
    import TimeZoneException as TimeZoneException
    import WeatherAPIException as WeatherAPIException

#
except ImportError:

    #
    from . import dt_management as dt_management

    # import the custom exceptions as Python modules
    from . import TimeZoneException as TimeZoneException
    from . import WeatherAPIException as WeatherAPIException

# from the needed Python modules import needed components
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtCore import Qt

# Definition of the 'WeatherWindow' class
class WeatherWindow(QMainWindow) :

     # Definition of the 'WeatherWindow' class constructor
     def __init__(self, timezone, title, width, height, weatherbit_api_key):
          
          # Definition of the main GUI
          super().__init__()

          #
          location = dt_management.geographical_coordinates_from_timezone(timezone)

          #
          if location != None :

               #
               weatherDatas = dt_management.get_Weather_from_Weather_bit(location, weatherbit_api_key)

               #
               if weatherDatas != None :
                    
                    #
                    weather_image = QPixmap()

                    #
                    weather_image.loadFromData(requests.get("https://www.weatherbit.io/static/img/icons/" + weatherDatas["data"][0]["weather"]["icon"] + ".png").content)

                    #
                    datetime_format_text =  "City : " + weatherDatas["data"][0]["city_name"] + "\n" \
                                            "Timezone : " + weatherDatas["data"][0]["timezone"] + "\n" \
                                            "Description : " + weatherDatas["data"][0]["weather"]["description"] + "\n" \
                                            "Clouds : " + str(weatherDatas["data"][0]["clouds"]) + "\n" \
                                            "Visibility (in km) : " + str(weatherDatas["data"][0]["vis"]) + "\n" \
                                            "Temperature (in °C) : " + str(weatherDatas["data"][0]["temp"]) + "\n" \
                                            "Apparent temperature (in °C) : " + str(weatherDatas["data"][0]["app_temp"]) + "\n" \
                                            "Dew point (in °C) : " + str(weatherDatas["data"][0]["dewpt"]) + "\n" \
                                            "Precipitation (in mm/h) : " + str(weatherDatas["data"][0]["precip"]) + "\n" \
                                            "Snow (in mm/h) : " + str(weatherDatas["data"][0]["snow"]) + "\n" \
                                            "Wind direction : " + weatherDatas["data"][0]["wind_cdir"] + "\n" \
                                            "Complete wind direction : " + weatherDatas["data"][0]["wind_cdir_full"] + "\n" \
                                            "Sunrise (UTC) : " + weatherDatas["data"][0]["sunrise"] + "\n" \
                                            "Sunset (UTC) : " + weatherDatas["data"][0]["sunset"] + "\n" \
                                            "UV : " + str(weatherDatas["data"][0]["uv"]) + "\n" \
                                            "Solar radiation (in W/m²) : " + str(weatherDatas["data"][0]["solar_rad"]) + "\n" \
                                            "Solar elevation angle (in °) : " + str(weatherDatas["data"][0]["elev_angle"]) + "\n" \
                                            "Air Quality Index : " + str(weatherDatas["data"][0]["aqi"]) + "\n" \
                                            ""

                    #
                    print(weatherDatas)

                    # 
                    self.setWindowTitle(title)

                    #
                    self.on_close_callback = None

                    #
                    self.setFixedSize(int(width), int(height))

                    # Implementation of the user guide GUI image
                    self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

                    #
                    self.image_label = QLabel(self)

                    #
                    self.image_label.setPixmap(weather_image)

                    #
                    self.text_label = QLabel(self)

                    #
                    self.text_label.setText(datetime_format_text)

                    #
                    self.text_label.setGeometry(20, 20, width - 40, height - 40)

                    #
                    self.text_label.setFont(
                        QFont("Calibri", 10, QFont.Bold)
                    )

                    #
                    self.text_label.setWordWrap(True)

                    #
                    central_widget = QWidget()

                    #
                    vertical_layout = QVBoxLayout()

                    #
                    vertical_layout.addWidget(self.image_label)
                    vertical_layout.addWidget(self.text_label)

                    #
                    central_widget.setLayout(vertical_layout)

                    #
                    self.setCentralWidget(central_widget)

               #
               else :

                    #
                    raise WeatherAPIException.WeatherAPIException("Weather not available !", 400)

          #
          else :
              
              #
              raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

     #
     def start(self):

        #
        self.show()

     #
     def closeEvent(self, event):

        #
        if self.on_close_callback :

            #
            self.on_close_callback()

        #
        event.accept()

          #
if __name__ == "__main__" :

     #
     app = QApplication(sys.argv)

     #
     weather_window = WeatherWindow()

     #
     weather_window.show()

     #
     sys.exit(app.exec())