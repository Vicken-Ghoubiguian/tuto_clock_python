# import the needed Python modules
import webview
import argparse

#
import dt_management as dt_management

# Definition of the 'CartographyWindow' class
class CartographyWindow():

    #
    def __init__(self, timezone, title, zoom, width, height):

        #
        location = dt_management.geographical_coordinates_from_timezone(timezone)

        #
        generated_map = dt_management.map_generator_for_location(location["latitude"], location["longitude"], zoom, "".join([location["location"]," location"]), location["location"], "generated_map_cartography_window.html")

        #
        self.window = webview.create_window(
            title=title,
            url=generated_map,
            width=int(width),
            height=int(height)
        )

    #
    def start(self):

        #
        webview.start()

# 
if __name__ == "__main__":

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
    args = parser.parse_args()

    #
    cw = CartographyWindow(args.timezone, args.title, args.zoom_map, args.width, args.height)

    #
    cw.start()