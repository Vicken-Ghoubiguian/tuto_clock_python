import dt_management
import TimeZoneException
import tkinter
import tkinter.ttk
import argparse

#
class Clock(tkinter.Tk) :

     #
     def __init__(self, timezone):
          
          #
          tkinter.Tk.__init__(self)

          #
          self.title("Clock")

          #
          self.iconbitmap("images/clock.ico")

          #
          self.resizable(False, False)

          #
          self.timezone = timezone

          #
          all_timezones = dt_management.get_all_timezones()

          #
          self.tz_comboBox = tkinter.ttk.Combobox(self, width = 110, values = all_timezones, state = "readonly")

          #
          self.tz_comboBox.set(self.timezone)

          #
          self.tz_comboBox.bind('<<ComboboxSelected>>', self.get_Selected_Item)

          #
          self.tz_comboBox.pack()

          #
          self.clock_label = tkinter.Label(self, font=('calibri', 40, 'bold'), background='blue', foreground='yellow')

          #
          self.clock_label.pack(anchor="center")

          #
          self.clock_time()

          #
          #menubar = tkinter.Menu(self)

          #
          #self.config(menu = menubar)

          #
          #timezone_menu = tkinter.Menu(menubar)

          #
          #all_timezones = dt_management.get_all_timezones()

          #
          #for current_timezone in all_timezones :

               #
          #     timezone_menu.add_command(
          #          label=current_timezone,
          #          command=self.destroy
          #     )

          #
          # menubar.add_cascade(
          #     label="timezones",
          #     menu=timezone_menu
          #)

     #
     def get_Selected_Item(self, eventObject) :

          #
          self.change_timezone(self.tz_comboBox.get())

     #
     def change_timezone(self, wished_timezone):

          print(wished_timezone)

          #
          #self.timezone = "Europe/Paris"

          #
          #self.clock_time()

     #
     def clock_time(self) :
               
          #
          self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(self.timezone).strftime(self.timezone + " : %Y-%m-%d %H:%M:%S"))

          #
          self.clock_label.after(1000, self.clock_time)

#
if __name__ == "__main__" :
     
     #
    parser = argparse.ArgumentParser(description="Simple app with timezones")

    #
    parser.add_argument('--timezone', action="store", dest='timezone', default=0)
    
    #
    args = parser.parse_args()

    #
    if dt_management.get_datetime_for_particular_timezone(args.timezone) != -1 :

         #
         clock = Clock(args.timezone)

    #
    else :
         
         #
         raise TimeZoneException.TimeZoneException("Timezone unknown !", 400)

    #
    clock.mainloop()