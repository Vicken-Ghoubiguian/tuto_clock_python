# import the needed Python modules
import sys
import argparse
import os

#
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont, QIcon


# Definition of the 'DateTimeFormatWindow' class
class DateTimeFormatWindow(QMainWindow) :

     # Definition of the 'DateTimeFormatWindow' class constructor
     def __init__(self, title, width, height):
          
          # Definition of the main GUI
          super().__init__()

          # 
          self.setWindowTitle(title)

          #
          self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

          #
          self.on_close_callback = None

          #
          self.setFixedSize(int(width), int(height))

          #
          self.datetime_format_label = QLabel(self)

          #
          self.datetime_format_label.setFont(
               QFont("Calibri", 10, QFont.Bold)
          )

          #
          self.datetime_format_label.setGeometry(20, 20, width - 40, height - 40)

          #
          datetime_format_text = "%a : abbreviated weekday name.\n" \
                                 "%A : full weekday name.\n" \
                                 "%w : weekday as a decimal number.\n" \
                                 "%d : day of the month as a zero added decimal.\n" \
                                 "%b : abbreviated month name.\n" \
                                 "%B : full month name.\n" \
                                 "%m : month as a zero added decimal number.\n" \
                                 "%y : year without century as a zero added decimal number.\n" \
                                 "%Y : year with century as a decimal number.\n" \
                                 "%H : hour (24-hour clock) as a zero added decimal number.\n" \
                                 "%I : hour (12-hour clock) as a zero added decimal number.\n" \
                                 "%p : locale’s AM or PM.\n" \
                                 "%M : minute as a zero added decimal number.\n" \
                                 "%S : second as a zero added decimal number.\n" \
                                 "%f : microsecond as a decimal number, zero added on the left.\n" \
                                 "%z : UTC offset in the form +HHMM or -HHMM.\n" \
                                 "%Z : time zone name.\n" \
                                 "%j : day of the year as a zero added decimal number.\n" \
                                 "%U : week number of the year (Sunday as the first day of the week).\n" \
                                 "%W : week number of the year (Monday as the first day of the week).\n" \
                                 "%c : locale’s appropriate date and time representation.\n" \
                                 "%x : locale’s appropriate date representation.\n" \
                                 "%X : locale’s appropriate time representation.\n" \
                                 "%% : A literal '%' character."

          #
          self.datetime_format_label.setText(datetime_format_text)

          #
          self.datetime_format_label.setWordWrap(True)

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
     parser = argparse.ArgumentParser(description="Simple app with timezones")

     #
     parser.add_argument('--title', action="store", dest='title', default="Datetime format")

     #
     parser.add_argument('--width', action="store", dest='width', default=500)

     #
     parser.add_argument('--height', action="store", dest='height', default=500)

     #
     args = parser.parse_args()

     #
     app = QApplication(sys.argv)

     #
     datetime_format_window = DateTimeFormatWindow(args.title, args.width, args.height)

     # Definition of the datetime format GUI image
     datetime_format_window.show()

     #
     sys.exit(app.exec())