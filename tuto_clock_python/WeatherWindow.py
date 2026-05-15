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
     def __init__(self):
          
          # Definition of the main GUI
          super().__init__()

          # 
          self.setWindowTitle("Weather window")

          #
          self.on_close_callback = None

          #
          self.setFixedSize(300, 300)

          # Implementation of the user guide GUI image
          self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

          #
          self.label = QLabel("Weather window", self)

          #
          self.label.setAlignment(Qt.AlignCenter)

          #
          self.setCentralWidget(self.label)

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