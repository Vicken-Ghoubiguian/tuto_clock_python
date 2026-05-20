#
import sys

# import the custom modules as Python modules
import tuto_clock_python.DatetimeFormatWindow as DatetimeFormatWindow

# import the QApplication widget from PySide
from PySide6.QtWidgets import QApplication

#
title = input("Entrez le titre que vous voulez pour afficher la fenêtre (ex: 'Datetime format') : ") or "Datetime format"

#
width = input("Entrez la largeur de la fenêtre (ex: 500) : ") or "500"

#
height = input("Entrez la hauteur de la fenêtre (ex: 500) : ") or "500"

#
app = QApplication(sys.argv)

#
datetime_format_window = DatetimeFormatWindow.DateTimeFormatWindow(title, int(width), int(height))

# Definition of the datetime format GUI image
datetime_format_window.show()

#
sys.exit(app.exec())