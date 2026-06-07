#
import sys

# import the custom modules as Python modules
import tuto_clock_python.UserGuideWindow as UserGuideWindow

# import the QApplication widget from PySide
from PySide6.QtWidgets import QApplication

#
title = input("Entrez le titre que vous voulez pour afficher la fenêtre (valeur par défaut: 'User guide') : ") or "Datetime format"

#
width = input("Entrez la largeur de la fenêtre (valeur par défaut: 500) : ") or "500"

#
height = input("Entrez la hauteur de la fenêtre (valeur par défaut: 500) : ") or "500"

#
app = QApplication(sys.argv)

#
user_guide_window = UserGuideWindow.UserGuideWindow(title, width, height)

# Definition of the user guide GUI image
user_guide_window.show()

#
sys.exit(app.exec())