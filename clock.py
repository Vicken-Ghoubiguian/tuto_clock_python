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
          def clock_time(timezone) :
               
               #
               self.clock_label.config(text=dt_management.get_datetime_for_particular_timezone(timezone).strftime(timezone + " : %Y-%m-%d %H:%M:%S"))

               #
               self.clock_label.after(1000, clock_time, timezone)

          #
          self.clock_label = tkinter.Label(self, font=('calibri', 40, 'bold'), background='blue', foreground='yellow')

          #
          self.clock_label.pack(anchor="center")

          #
          clock_time(timezone)

          #
          menubar = tkinter.Menu(self)

          #
          self.config(menu = menubar)

          #
          file_menu = tkinter.Menu(menubar)

          #
          all_timezones = dt_management.get_all_timezones()

          #
          for current_timezone in all_timezones :

               #
               file_menu.add_command(
                    label=current_timezone,
                    command=self.destroy
               )

          #
          menubar.add_cascade(
               label="timezones",
               menu=file_menu
          )

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