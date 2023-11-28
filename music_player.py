from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QSlider, QPushButton, QDial
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("music_player.ui", self)

        # Define Our Widgets
        self.musicName = self.findChild(QLabel, "musicName")
        self.artistName = self.findChild(QLabel, "artistName")
        self.musicTimer = self.findChild(QSlider, "musictimer")
        self.startCount = self.findChild(QLabel, "counterStart")
        self.endCount = self.findChild(QLabel, "counterEnd")
        self.playPauseButton = self.findChild(QPushButton, "playButton")
        self.forwardButton = self.findChild(QPushButton, "forwardButton")
        self.backwardButton = self.findChild(QPushButton, "backwardButton")
        self.shuffleButton = self.findChild(QPushButton, "shuffleButton")
        self.repeatButton = self.findChild(QPushButton, "repeatButton")
        self.volume = self.findChild(QDial, "volume")
        self.volumeLabel = self.findChild(QLabel, "volumeLabel")
        self.listButton = self.findChild(QPushButton, "listButton")

        # 

        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIMainWindow = UI()
app.exec_()

