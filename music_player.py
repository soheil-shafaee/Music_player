from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("music_player.ui", self)

        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIMainWindow = UI()
app.exec_()

