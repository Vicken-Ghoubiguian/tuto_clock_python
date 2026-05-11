# import the needed Python modules
import webview

#
import dt_management as dt_management

# Definition of the 'CartographyWindow' class
class CartographyWindow():

    #
    def __init__(self, timezone, title, zoom):

        #
        location = dt_management.geographical_coordinates_from_timezone(timezone)

        #
        generated_map = dt_management.map_generator_for_location(location["latitude"], location["longitude"], zoom, "".join([location["location"]," location"]), location["location"], "generated_map_cartography_window.html")

        #
        self.window = webview.create_window(
            title=title,
            url=generated_map,
            width=1200,
            height=800
        )

    #
    def start(self):

        #
        webview.start()

if __name__ == "__main__":

    cw = CartographyWindow("Europe/Paris", "test", 15)

    cw.start()