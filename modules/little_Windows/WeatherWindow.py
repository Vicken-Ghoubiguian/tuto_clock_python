# import the needed Python modules
import tkinter
import tkinter.ttk
import os

# from the needed Python modules import needed components
from PIL import Image, ImageTk

# Definition of the 'WeatherWindow' class
class WeatherWindow(tkinter.Tk) :

     # Definition of the 'WeatherWindow' class constructor
     def __init__(self):
          
          # Definition of the main GUI
          tkinter.Tk.__init__(self)

          # 
          self.title("Weather")

          #
          self.resizable(False, False)

          #
          self.geometry('300x300')

          #
if __name__ == "__main__" :

     #
     weather_window = WeatherWindow()

     # Definition of the weather GUI image
     weather_window_gui_image = ImageTk.PhotoImage(Image.open(os.path.join("..", "..", "images", "clock.png")))

     # Implementation of the user guide GUI image
     weather_window.iconphoto(True, weather_window_gui_image)

     #
     weather_window.mainloop()