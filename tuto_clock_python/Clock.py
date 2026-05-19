#
try :

     # import the dt_management module as a Python module
     import dt_management as dt_management

     # import the windows as Python modules
     import CartographyWindow as CartographyWindow
     import WeatherWindow as WeatherWindow
     import DatetimeFormatWindow as DatetimeFormatWindow
     import UserGuideWindow as UserGuideWindow

     # import the custom exceptions as Python modules
     import TimeZoneException as TimeZoneException
     import OpenedWindowException as OpenedWindowException

     # import the LittleWindowTypeEnum enum as Python module
     import LittleWindowTypeEnum as LittleWindowTypeEnum

#
except ImportError:

     # import the dt_management module as a Python module
     from . import dt_management as dt_management

     # import the windows as Python modules
     from . import CartographyWindow as CartographyWindow
     from . import WeatherWindow as WeatherWindow
     from . import DatetimeFormatWindow as DatetimeFormatWindow
     from . import UserGuideWindow as UserGuideWindow

     # import the custom exceptions as Python modules
     from . import TimeZoneException as TimeZoneException
     from . import OpenedWindowException as OpenedWindowException

     # import the LittleWindowTypeEnum enum as Python module
     from . import LittleWindowTypeEnum as LittleWindowTypeEnum

# from the needed Python modules import needed components
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QMenuBar, QMenu
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QTimer, Qt

import argparse
import os
import sys

class Clock(QApplication):

    def __init__(self, timezone, dt_format, zoom_map, title, width, height):

        super().__init__(sys.argv)

        self.timezone = timezone
        self.datetime_format = dt_format
        self.initial_datetime_format = dt_format

        self.littleWindow = False
        self.littleWindowOpened = False

        # MAIN WINDOW
        self.window = QMainWindow()
        self.window.setWindowTitle(title)
        self.window.setFixedSize(int(width), int(height))
        self.window.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

        self.window.setWindowFlags(
            Qt.Window |
            Qt.WindowTitleHint
        )

        # COMBOBOX timezone
        self.tz_comboBox = QComboBox(self.window)
        self.tz_comboBox.setGeometry(10, 10, 1480, 25)

        self.tz_comboBox.addItems(dt_management.get_all_timezones())
        self.tz_comboBox.setCurrentText(self.timezone)
        self.tz_comboBox.currentTextChanged.connect(self.get_Selected_Timezone)

        # ENTRY datetime format
        self.dt_format_entry = QLineEdit(self.window)
        self.dt_format_entry.setGeometry(10, 45, 1480, 25)
        self.dt_format_entry.setText(self.datetime_format)
        self.dt_format_entry.textChanged.connect(self.get_Selected_Datetime_format)

        # LABEL clock
        self.clock_label = QLabel(self.window)
        self.clock_label.setGeometry(10, 100, 1480, 200)
        self.clock_label.setFont(QFont("Calibri", 40, QFont.Bold))
        self.clock_label.setStyleSheet("""
               color: gold;
               background-color: blue;
          """)

        # MENU
        menubar = QMenuBar(self.window)
        menu = QMenu("Menu", self.window)

        #
        cartographyAction = menu.addAction("Cartography")
        weatherAction = menu.addAction("Weather")
        dateTimeFormatsAction = menu.addAction("Datetime formats")
        userGuideAction = menu.addAction("User guide")

        #
        menu.addAction("Exit", self.window.close)

        openCartographyWindowCallback = lambda: self.openWindow(LittleWindowTypeEnum.LittleWindowTypeEnum.CARTOGRAPHY)
        openWeatherWindowCallback = lambda: self.openWindow(LittleWindowTypeEnum.LittleWindowTypeEnum.WEATHER)
        openDateTimeFormatsWindowCallback = lambda: self.openWindow(LittleWindowTypeEnum.LittleWindowTypeEnum.DATETIMEFORMATS)
        openUserGuideWindowCallback = lambda: self.openWindow(LittleWindowTypeEnum.LittleWindowTypeEnum.USERGUIDE)

        #
        cartographyAction.triggered.connect(openCartographyWindowCallback)
        weatherAction.triggered.connect(openWeatherWindowCallback)
        dateTimeFormatsAction.triggered.connect(openDateTimeFormatsWindowCallback)
        userGuideAction.triggered.connect(openUserGuideWindowCallback)

        #
        menubar.addMenu(menu)
        #self.window.setMenuBar(menubar)

        # TIMER (remplace after())
        self.timer = QTimer()
        self.timer.timeout.connect(self.clock_time)
        self.timer.start(1000)

        self.clock_time()

    # OPEN WINDOWS
    def openWindow(self, littleWindowTypeEnum):

        #
        if not self.littleWindowOpened:

            #
            if littleWindowTypeEnum == LittleWindowTypeEnum.LittleWindowTypeEnum.CARTOGRAPHY :

                #
                self.littleWindow = CartographyWindow.CartographyWindow(self.timezone, "World's map", 5, 1200, 800, "generated_map_clock.html")

            #
            elif littleWindowTypeEnum == LittleWindowTypeEnum.LittleWindowTypeEnum.WEATHER :

                #
                self.littleWindow = WeatherWindow.WeatherWindow()

            #
            elif littleWindowTypeEnum == LittleWindowTypeEnum.LittleWindowTypeEnum.DATETIMEFORMATS :

                #
                self.littleWindow = DatetimeFormatWindow.DateTimeFormatWindow("Datetime format", 500, 500)

            #
            elif littleWindowTypeEnum == LittleWindowTypeEnum.LittleWindowTypeEnum.USERGUIDE :

                #
                self.littleWindow = UserGuideWindow.UserGuideWindow("User Guide", 300, 300)

            #
            self.littleWindow.on_close_callback = self.closeWindow
            self.littleWindowOpened = True
            self.tz_comboBox.setEnabled(False)
            self.dt_format_entry.setEnabled(False)
            self.littleWindow.start()

        else:
            raise OpenedWindowException.OpenedWindowException("Window already opened !", 400)

    def closeWindow(self):

        self.littleWindowOpened = False
        self.littleWindow = False
        self.tz_comboBox.setEnabled(True)
        self.dt_format_entry.setEnabled(True)

    # EVENTS
    def get_Selected_Datetime_format(self):
        self.datetime_format = self.dt_format_entry.text()

    def get_Selected_Timezone(self):
        self.timezone = self.tz_comboBox.currentText()

    # CLOCK UPDATE
    def clock_time(self):

        #
        dt = dt_management.get_datetime_for_particular_timezone(self.timezone)

        #
        country = dt_management.get_datas_from_particular_countrycode(dt_management.get_countrycode_of_timezone(self.timezone))

        #
        if dt is None:

            #   
            return

        #
        if country is not None :

          # Display the timezone with its datetime and the country
          self.clock_label.setText(
               f"{country["flag"].encode('utf-8').decode('unicode_escape')} {self.timezone} ({country["name"]}) : {dt.strftime(self.datetime_format)}"
          )

        #
        else :
          
          #
          self.clock_label.setText(
               f"{self.timezone} : {dt.strftime(self.datetime_format)}"
          )

    def run(self):

        self.window.show()
        sys.exit(self.exec())


# MAIN
if __name__ == "__main__":

    iana_tz = dt_management.return_iana_timezone()

    parser = argparse.ArgumentParser()
    parser.add_argument('--timezone', default=iana_tz)
    parser.add_argument('--dt_format', default='%Y-%m-%d %H:%M:%S')
    parser.add_argument('--zoom_map', default=5)
    parser.add_argument('--width', default=1500)
    parser.add_argument('--height', default=500)
    parser.add_argument('--title', default='Clock')

    args = parser.parse_args()

    if dt_management.get_datetime_for_particular_timezone(args.timezone) is None:
        raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

    clock = Clock(
        args.timezone,
        args.dt_format,
        args.zoom_map,
        args.title,
        args.width,
        args.height
    )

    clock.run()