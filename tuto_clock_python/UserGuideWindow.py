# import the needed Python modules
import sys
import argparse
import os

# from the needed Python modules import needed components
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

# Definition of the 'UserGuideWindow' class
class UserGuideWindow(QMainWindow) :

     # Definition of the 'UserGuideWindow' class constructor
     def __init__(self, title, width, height):
          
          # Definition of the main GUI
          super().__init__()

          # 
          self.setWindowTitle(title)

          #
          self.setFixedSize(int(width), int(height))

          #
          self.on_close_callback = None

          # Implementation of the user guide GUI image
          self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

          #
          self.label = QLabel("User Guide", self)

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

if __name__ == "__main__" :

     #
     parser = argparse.ArgumentParser(description="Simple app with timezones")

     #
     parser.add_argument('--title', action="store", dest='title', default='User Guide')

     #
     parser.add_argument('--width', action="store", dest='width', default=300)

     #
     parser.add_argument('--height', action="store", dest='height', default=300)

     #
     args = parser.parse_args()

     #
     app = QApplication(sys.argv)

     #
     user_guide_window = UserGuideWindow(args.title, args.width, args.height)

     #
     user_guide_window.show()

     #
     sys.exit(app.exec())