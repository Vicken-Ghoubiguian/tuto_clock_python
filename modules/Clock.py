# import the needed Python modules
import dt_management as dt_management
import TimeZoneException as TimeZoneException
import tkinter
import tkinter.ttk
import argparse

# from the needed Python modules import needed components
from tzlocal.windows_tz import win_tz

# Definition of the 'Clock' class
class Clock(tkinter.Tk) :

     # Definition of the 'Clock' class constructor
     def __init__(self, timezone):
          
          # Definition of the main GUI
          tkinter.Tk.__init__(self)

          # Definition of the main GUI title
          self.title("Clock")

          # Instruction that disables the ‘X’ (close) button in the top-right corner of the window.
          self.protocol('WM_DELETE_WINDOW', 'break')

          # Definition of the main GUI image
          self.iconbitmap("../images/clock.ico")

          #
          self.resizable(False, False)

          #
          self.timezone = timezone

          #
          self.datetime_format = "%Y-%m-%d %H:%M:%S"

          #
          all_timezones = dt_management.get_all_timezones()

          #
          self.tz_comboBox = tkinter.ttk.Combobox(self, width = 110, values = all_timezones, state = "readonly")

          #
          self.tz_comboBox.set(self.timezone)

          #
          self.tz_comboBox.bind('<<ComboboxSelected>>', self.get_Selected_Timezone)

          #
          self.tz_comboBox.pack()

          #
          self.dt_format_comboBox = tkinter.ttk.Combobox(self, width = 110, values = ["%A %B %d %Y %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%m %d %Y %H:%M:%S"], state = "readonly")

          #
          self.dt_format_comboBox.set(self.datetime_format)

          #
          self.dt_format_comboBox.bind('<<ComboboxSelected>>', self.get_Selected_Datetime_format)

          #
          self.dt_format_comboBox.pack()

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

          #
          timezone_menu.add_command(
               label="Exit",
               command=self.destroy
          )

          #
          menubar.add_cascade(
               label="menu",
               menu=timezone_menu
          )

     #
     def get_Selected_Datetime_format(self, eventObject) :

          #
          self.datetime_format = self.dt_format_comboBox.get()

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
               self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(self.timezone).strftime(self.timezone + " (" + dt_management.get_countrycode_of_timezone(self.timezone) + ") : " + self.datetime_format))

          #
          else :

               #
               self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(self.timezone).strftime(self.timezone + " : " + self.datetime_format))

          #
          self.clock_label.after(1000, self.clock_time)

#
if __name__ == "__main__" :
    
    #
    iana_tz = win_tz.get("Romance Standard Time")
     
     #
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=iana_tz)
    
    #
    args = parser.parse_args()

    #
    if dt_management.get_datetime_for_particular_timezone(args.timezone) != None :

         #
         clock = Clock(args.timezone)

    #
    else :
         
         #
         raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

    #
    clock.mainloop()