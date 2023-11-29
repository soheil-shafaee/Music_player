from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QSlider, QPushButton, QDial, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl
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
        self.setFixedSize(413, 600)
        self.djPix = QPixmap("image/dj-fotor-202311281363.png")
        self.defaultImage.setPixmap(self.djPix)
        self.playButton.setIcon(QIcon("feather/play.svg"))
        self.pauseButton.setIcon(QIcon("feather/pause-circle.svg"))
        self.stopButton.setIcon(QIcon("feather/stop-circle.svg"))
        self.forwardButton.setIcon(QIcon("feather/skip-forward.svg"))
        self.backwardButton.setIcon(QIcon("feather/skip-back.svg"))
        self.shuffleButton.setIcon(QIcon("feather/shuffle.svg"))
        self.repeatButton.setIcon(QIcon("feather/repeat.svg"))
        self.listButton.setIcon(QIcon("feather/gitlab.svg"))

        # Set Default Value For volume
        self.volume.setValue(50)

        # Click The Button
        self.volume.valueChanged.connect(self.volumeChange)
        self.playButton.clicked.connect(self.play)
        self.pauseButton.clicked.connect(self.pause)
        self.stopButton.clicked.connect(self.stop)
        self.forwardButton.clicked.connect(self.forward)
        self.backwardButton.clicked.connect(self.back)
        self.shuffleButton.clicked.connect(self.shuffle)

        # Media Player
        self.player = QMediaPlayer()
        self.playList = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playList)

        # Show The App
        self.show()

    # Define Function To Change Volume
    def volumeChange(self):
        valueVolume = self.volume.value()
        self.volumeLabel.setText(str(valueVolume))
        self.player.setVolume(valueVolume)

    # Define The Play Function:
    def play(self):
        file = QFileDialog(self)
        file.setNameFilter("MP3 Files (*.mp3);; All Files (*)")
        file.setWindowTitle("Add Music")
        file.setFileMode(QFileDialog.ExistingFiles)
        if self.playList.isEmpty():
            if file.exec_():
                choose_files = file.selectedFiles()
                if choose_files:
                    for file in choose_files:
                        file_url = QUrl.fromLocalFile(file)
                        content = QMediaContent(file_url)
                        self.playList.addMedia(content)

                    self.player.play()
                    self.changeName()
        else:
            self.player.play()

    # Define Function To Change The name and artist music
    def changeName(self):
        songInfo = self.player.currentMedia().canonicalUrl().fileName().split("-")
        if len(songInfo) == 2:
            self.musicName.setText(songInfo[1])
            self.artistName.setText(songInfo[0])

    # Define Function For pause The music
    def pause(self):
        self.player.pause()

    # Define Function For Stop The music
    def stop(self):
        self.player.stop()

    # Define Function For Forward The music
    def forward(self):
        self.playList.next()
        self.changeName()

    # Define Function for Back To the Previous Music
    def back(self):
        self.playList.previous()
        self.changeName()

    # Define Function For Shuffle The List of Music
    def shuffle(self):
        self.playList.shuffle()
        self.changeName()


# Initialize The App
app = QApplication(sys.argv)
UIMainWindow = UI()
app.exec_()
