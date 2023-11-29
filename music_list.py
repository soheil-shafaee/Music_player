from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QPushButton
from PyQt5 import uic
import sys


class musicList(QMainWindow):
    def __init__(self):
        super(musicList, self).__init__()

        # Load The File
        uic.loadUi("music_list.ui", self)

        # Fix The Size of Window
        self.setFixedSize(412, 436)

        # Define Our Widgets

        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = musicList()
app.exec_()
