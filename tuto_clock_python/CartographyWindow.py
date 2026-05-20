# import the needed Python modules
import argparse
import os
import sys

# from the needed Python modules import needed components
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import QUrl

#
try :

    #
    import dt_management as dt_management

    # import the custom exceptions as Python modules
    import TimeZoneException as TimeZoneException

#
except ImportError:

    #
    from . import dt_management as dt_management

    # import the custom exceptions as Python modules
    from . import TimeZoneException as TimeZoneException

# Definition of the 'CartographyWindow' class
class CartographyWindow(QWebEngineView):

    #
    def __init__(self, timezone, title, zoom, width, height, file):

        #
        super().__init__()

        #
        self.settings().setAttribute(
            QWebEngineSettings.LocalContentCanAccessRemoteUrls,
            True
        )

        #
        self.settings().setAttribute(
            QWebEngineSettings.LocalContentCanAccessFileUrls,
            True
        )

        #
        self.on_close_callback = None

        #
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "clock.png")))

        #
        location = dt_management.geographical_coordinates_from_timezone(timezone)

        #
        if location != None :

            #
            generated_map = dt_management.map_generator_for_location(location["latitude"], location["longitude"], zoom, "".join([location["location"]," location"]), location["location"], file)

            #
            self.setWindowTitle(title)

            #
            self.setFixedSize(int(width), int(height))

            #
            self.load(QUrl.fromLocalFile(generated_map))

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
if __name__ == "__main__":

    #
    app = QApplication(sys.argv)

    # Get the system's (platform's) timezone
    iana_tz = dt_management.return_iana_timezone()

    #
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=iana_tz)

    #
    parser.add_argument('--title', action="store", dest='title', default='World\'s map')

    #
    parser.add_argument('--zoom_map', action="store", dest='zoom_map', default=5)

    #
    parser.add_argument('--width', action="store", dest='width', default=1200)

    #
    parser.add_argument('--height', action="store", dest='height', default=800)

    #
    parser.add_argument('--file', action="store", dest='file', default='generated_map_cartography_window.html')

    #
    args = parser.parse_args()

    #
    cw = CartographyWindow(args.timezone, args.title, args.zoom_map, args.width, args.height, args.file)

    #
    cw.start()

    #
    sys.exit(app.exec())