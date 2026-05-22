# import the needed Python modules
import sys
import os

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
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QIcon
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
                    self.label = QLabel("https://www.weatherbit.io/static/img/icons/ICON.png", self)

                    #
                    self.label.setAlignment(Qt.AlignCenter)

                    #
                    self.setCentralWidget(self.label)

                    #

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