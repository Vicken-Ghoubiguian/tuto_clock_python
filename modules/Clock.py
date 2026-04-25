# import the needed Python modules
import dt_management as dt_management
import tkinter
import tkinter.ttk
import argparse
import os

# import the windows as Python modules
import little_Windows.WeatherWindow
import little_Windows.DatetimeFormatWindow
import little_Windows.UserGuideWindow

# import the custom exceptions as Python modules
import custom_Exceptions.TimeZoneException as TimeZoneException
import custom_Exceptions.OpenedWindowException as OpenedWindowException

# from the needed Python modules import needed components
from tzlocal.windows_tz import win_tz
from PIL import Image, ImageTk

# Definition of the 'Clock' class
class Clock(tkinter.Tk) :

     # Definition of the 'Clock' class constructor
     def __init__(self, timezone, dt_format):
          
          # Definition of the main GUI
          tkinter.Tk.__init__(self)

          # Definition of the main GUI title
          self.title("Clock")

          # Instruction that disables the ‘X’ (close) button in the top-right corner of the window.
          self.protocol('WM_DELETE_WINDOW', 'break')

          # Definition of the main GUI image
          self.gui_image = ImageTk.PhotoImage(Image.open(os.path.join("..", "images", "clock.png")))

          # Implementation of the main GUI image
          self.iconphoto(True, self.gui_image)

          # Definition of the window dimensions
          self.geometry('1500x500')

          # Set the window not resizable
          self.resizable(False, False)

          # Set the current timezone the same as filled in argument
          self.timezone = timezone

          # Set the initial datetime format
          self.initial_datetime_format = dt_format

          # Set the current datetime format as the initial one
          self.datetime_format = self.initial_datetime_format

          # There is no window which is opened (class attribute 'littleWindow' as False)
          self.littleWindow = False

          # Get all available timezones into the 'all_timezones' variable
          all_timezones = dt_management.get_all_timezones()

          # Definition of the 'tz_comboBox' combobox which is the combobox of all timezones
          self.tz_comboBox = tkinter.ttk.Combobox(self, width = 110, values = all_timezones, state = "readonly")

          #
          self.tz_comboBox.set(self.timezone)

          #
          self.tz_comboBox.bind('<<ComboboxSelected>>', self.get_Selected_Timezone)

          #
          self.tz_comboBox.pack()

          #
          self.dt_format_entry = tkinter.Entry(self, width = 113)

          #
          self.dt_format_entry.insert(0, self.datetime_format)

          #
          self.dt_format_entry.bind('<Return>', self.get_Selected_Datetime_format)

          #
          self.dt_format_entry.pack()

          #
          self.clock_label = tkinter.Label(self, font=('calibri', 40, 'bold'), background='blue', foreground='yellow')

          #
          self.clock_label.pack(anchor="center")

          #
          self.clock_time()

          #
          menubar = tkinter.Menu(self)

          #
          self.config(menu = menubar)

          #
          timezone_menu = tkinter.Menu(menubar)

          # Definition of the 'Weather' menu command to display weather of the current timezone location
          timezone_menu.add_command(
               label="Weather",
               command=self.openWeatherWindow
          )

          # Definition of the 'Datetime formats' menu command to inform the user about the datetime formats that could be use in the application
          timezone_menu.add_command(
               label="Datetime formats",
               command=self.openDatetimeFormatWindow
          )

          # Definition of the 'User guide' menu command to guide the user on the application features
          timezone_menu.add_command(
               label="User guide",
               command=self.openUserGuideWindow
          )

          # Definition of the 'Exit' menu command to exit the application
          timezone_menu.add_command(
               label="Exit",
               command=self.destroy
          )

          # Definition of the 'menu' menu
          menubar.add_cascade(
               label="menu",
               menu=timezone_menu
          )

     #
     def openWeatherWindow(self) :

          #
          if self.littleWindow == False :

               #
               self.littleWindow = tkinter.Tk()

               #
               self.littleWindow.title("Weather")

               #
               self.littleWindow.resizable(False, False)

               #
               self.littleWindow.geometry('300x300')

               #
               self.littleWindow.wm_protocol("WM_DELETE_WINDOW", self.closeWindow)

               #
               self.littleWindow.mainloop()

          #
          else :

               #
               raise OpenedWindowException.OpenedWindowException("Window already opened !", 400)

     #
     def openDatetimeFormatWindow(self) :

          #
          if self.littleWindow == False :

               # Definition of the 'DateTimeFormatWindow' window to inform the user about the different available datetime formats
               self.littleWindow = little_Windows.DatetimeFormatWindow.DateTimeFormatWindow()

               #
               self.littleWindow.wm_protocol("WM_DELETE_WINDOW", self.closeWindow)

               #
               self.littleWindow.mainloop()

          #
          else :

               #
               raise OpenedWindowException.OpenedWindowException("Window already opened !", 400)

     #
     def openUserGuideWindow(self) :

          #
          if self.littleWindow == False :

               # Definition of the 'UserGuideWindow' window to inform the user about the clock features
               self.littleWindow = little_Windows.UserGuideWindow.UserGuideWindow()

               #
               self.littleWindow.wm_protocol("WM_DELETE_WINDOW", self.closeWindow)

               #
               self.littleWindow.mainloop()

          #
          else :

               #
               raise OpenedWindowException.OpenedWindowException("Window already opened !", 400)

     #
     def closeWindow(self) :

          #
          self.littleWindow.destroy()

          #
          self.littleWindow = False

     #
     def get_Selected_Datetime_format(self, eventObject) :

          #
          self.datetime_format = self.dt_format_entry.get()

          #
          self.clock_time()

     #
     def get_Selected_Timezone(self, eventObject) :

          #
          self.timezone = self.tz_comboBox.get()

          #
          self.clock_time()

     #
     def clock_time(self) :

          #
          if dt_management.get_countrycode_of_timezone(self.timezone) != None :
               
               #
               try :

                    #
                    country = dt_management.get_datas_from_particular_countrycode(dt_management.get_countrycode_of_timezone(self.timezone))

                    #
                    unicode_country = country["flag"].encode('utf-8')

                    #
                    self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(self.timezone).strftime(self.timezone + " (" + unicode_country.decode('unicode_escape') + " " + country["name"] + ") : " + self.datetime_format))

               #
               except :

                    #
                    self.datetime_format = self.initial_datetime_format

                    #
                    country = dt_management.get_datas_from_particular_countrycode(dt_management.get_countrycode_of_timezone(self.timezone))

                    #
                    unicode_country = country["flag"].encode('utf-8')

                    #
                    self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(self.timezone).strftime(self.timezone + " (" + unicode_country.decode('unicode_escape') + " " + country["name"] + ") : " + self.datetime_format))

          #
          else :

               #
               self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(self.timezone).strftime(self.timezone + " : " + self.datetime_format))

          #
          self.clock_label.after(1000, self.clock_time)

#
if __name__ == "__main__" :
    
    #
    iana_tz = dt_management.return_iana_timezone()

     #
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=iana_tz)

    #
    parser.add_argument('--dt_format', action="store", dest='dt_format', default='%Y-%m-%d %H:%M:%S')
    
    #
    args = parser.parse_args()

    #
    if dt_management.get_datetime_for_particular_timezone(args.timezone) != None :

         #
         clock = Clock(args.timezone, args.dt_format)

    #
    else :
         
         #
         raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

    #
    clock.mainloop()