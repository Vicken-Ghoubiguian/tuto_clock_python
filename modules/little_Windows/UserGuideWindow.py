# import the needed Python modules
import tkinter
import tkinter.ttk
import os

# from the needed Python modules import needed components
from PIL import Image, ImageTk

# Definition of the 'UserGuideWindow' class
class UserGuideWindow(tkinter.Tk) :

     # Definition of the 'UserGuideWindow' class constructor
     def __init__(self):
          
          # Definition of the main GUI
          tkinter.Tk.__init__(self)

          # 
          self.title("User Guide")

          #
          self.resizable(False, False)

          #
          self.geometry('300x300')

          #
if __name__ == "__main__" :

     #
     user_guide_window = UserGuideWindow()

     # Definition of the datetime format GUI image
     user_guide_gui_image = ImageTk.PhotoImage(Image.open(os.path.join("..", "..", "images", "clock.png")))

     # Implementation of the user guide GUI image
     user_guide_window.iconphoto(True, user_guide_gui_image)

     #
     user_guide_window.mainloop()