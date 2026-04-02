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
if __name__ == "__main__":
     
     #
     clock = Clock()

     #
     clock.mainloop()