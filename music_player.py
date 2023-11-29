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
        self.defaultImage = self.findChild(QLabel, "defualtImage")
        self.musicName = self.findChild(QLabel, "musicName")
        self.artistName = self.findChild(QLabel, "artistName")
        self.musicTimer = self.findChild(QSlider, "musictimer")
        self.startCount = self.findChild(QLabel, "counterStart")
        self.endCount = self.findChild(QLabel, "counterEnd")
        self.playButton = self.findChild(QPushButton, "playButton")
        self.pauseButton = self.findChild(QPushButton, "pauseButton")
        self.stopButton = self.findChild(QPushButton, "stopButton")
        self.forwardButton = self.findChild(QPushButton, "forwardButton")
        self.backwardButton = self.findChild(QPushButton, "backwardButton")
        self.shuffleButton = self.findChild(QPushButton, "shuffleButton")
        self.repeatButton = self.findChild(QPushButton, "repeatButton")
        self.volume = self.findChild(QDial, "volume")
        self.volumeLabel = self.findChild(QLabel, "volumeLabel")
        self.listButton = self.findChild(QPushButton, "listButton")

        # Put Icon and Image Into Music player App
        self.setWindowIcon(QIcon("image/cassette.gif"))
        self.setFixedSize(413, 590)
        self.djPix = QPixmap("image/dj-fotor-202311281363.png")
        self.defaultImage.setPixmap(self.djPix)
        self.playButton.setIcon(QIcon("feather/play.svg"))
        self.pauseButton.setIcon(QIcon("feather/pause-circle.svg"))
        self.stopButton.setIcon(QIcon("feather/stop-circle.svg"))
        self.forwardButton.setIcon(QIcon("feather/skip-forward.svg"))
        self.backwardButton.setIcon(QIcon("feather/skip-back.svg"))
        self.shuffleButton.setIcon(QIcon("feather/shuffle.svg"))
        self.repeatButton.setIcon(QIcon("feather/repeat.svg"))

        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIMainWindow = UI()
app.exec_()
