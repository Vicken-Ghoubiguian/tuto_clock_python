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

          #
          self.resizable(False, False)

          #
          self.geometry('500x400')

          #
          self.datetime_format_label = tkinter.Label(self, font=('calibri', 10, 'bold'))

          #
          self.datetime_format_label.pack(pady=0, padx=0, anchor="w")

          #
          datetime_format_text = "%a : abbreviated weekday name.\n" \
                                 "%A : full weekday name.\n" \
                                 "%w : weekday as a decimal number.\n" \
                                 "%d : day of the month as a zero added decimal.\n" \
                                 "%b : abbreviated month name.\n" \
                                 "%B : full month name.\n" \
                                 "%m : month as a zero added decimal number.\n" \
                                 "%y : year without century as a zero added decimal number.\n" \
                                 "%Y : year with century as a decimal number.\n" \
                                 "%H : hour (24-hour clock) as a zero added decimal number.\n" \
                                 "%I : hour (12-hour clock) as a zero added decimal number.\n" \
                                 "%p : locale’s AM or PM.\n" \
                                 "%M : minute as a zero added decimal number.\n" \
                                 "%S : second as a zero added decimal number.\n" \
                                 "%f : microsecond as a decimal number, zero added on the left.\n" \
                                 "%z : UTC offset in the form +HHMM or -HHMM.\n" \
                                 "%Z : time zone name.\n" \
                                 "%j : day of the year as a zero added decimal number.\n" \
                                 "%U : week number of the year (Sunday as the first day of the week).\n" \
                                 "%W : week number of the year (Monday as the first day of the week).\n" \
                                 "%c : locale’s appropriate date and time representation.\n" \
                                 "%x : locale’s appropriate date representation.\n" \
                                 "%X : locale’s appropriate time representation.\n" \
                                 "%% : A literal '%' character."

          #
          self.datetime_format_label.config(text=datetime_format_text)

#
if __name__ == "__main__" :

     #
     datetime_format_window = DateTimeFormatWindow()

     # Definition of the main GUI image
     datetime_format_window.iconbitmap(os.path.join("..", "..", "images", "clock.ico"))

     #
     datetime_format_window.mainloop()