import dt_management
import tkinter
import tkinter.ttk

#
class Clock(tkinter.Tk) :
     
     #
     def __init__(self):
          
          #
          tkinter.Tk.__init__(self)

          #
          self.title("Clock")

          #
          def clock_time() :
               
               #
               clock_label.config(text=dt_management.get_datetime_for_particular_timezone("Europe/Paris").strftime("%Y-%m-%d %H:%M:%S"))

               #
               clock_label.after(1000, clock_time)

          #
          clock_label = tkinter.Label(self, font=('calibri', 40, 'bold'), background='blue', foreground='yellow')

          #
          clock_label.pack(anchor="center")

          #
          clock_time()

#
if __name__ == "__main__" :
     
     #
     clock = Clock()

     #
     clock.mainloop()