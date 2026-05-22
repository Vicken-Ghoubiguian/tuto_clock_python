# import the needed Python modules
import sys
import os

# from the needed Python modules import needed components
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

# Definition of the 'WeatherWindow' class
class WeatherWindow(QMainWindow) :

     # Definition of the 'WeatherWindow' class constructor
     def __init__(self, title, width, height, weatherbit_api_key):
          
          # Definition of the main GUI
          super().__init__()

          # 
          self.setWindowTitle(title)

          #
          self.on_close_callback = None

          #
          self.setFixedSize(int(width), int(height))

          # Implementation of the user guide GUI image
          self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

          #
          self.label = QLabel("https://api.weatherbit.io/v2.0/current?lat=-22.5776104&lon=17.0772739&key=API_KEY https://www.weatherbit.io/static/img/icons/ICON.png", self)

          #
          self.label.setAlignment(Qt.AlignCenter)

          #
          self.setCentralWidget(self.label)

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