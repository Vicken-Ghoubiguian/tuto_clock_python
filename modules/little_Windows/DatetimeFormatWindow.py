# import the needed Python modules
import tkinter
import tkinter.ttk
import os

# Definition of the 'DateTimeFormatWindow' class
class DateTimeFormatWindow(tkinter.Tk) :

     # Definition of the 'DateTimeFormatWindow' class constructor
     def __init__(self):
          
          # Definition of the main GUI
          tkinter.Tk.__init__(self)

          # 
          self.title("Datetime format")

          # Definition of the main GUI image
          self.iconbitmap(os.path.join("..", "images", "clock.ico"))

          #
          self.resizable(False, False)

          #
          self.geometry('300x300')