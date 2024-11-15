
from PyQt6.QtWidgets import QApplication, QStackedWidget
from MuseumDesign import Ui_StackedWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from MuseumDesign import Ui_StackedWidget

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)
        self.setCurrentIndex(0)
        self.votes = [0, 0, 0]
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile("/Users/quangvinh/Documents/Pythonfile/thiencooksdinner/Baotangcuasutiecnuoi/imageforproject/image/Beethoven - Moonlight Sonata (1st Movement).mp3"))
        self.painting_names = ["Late afternoon, Vetheuil", "Cô gái bên hoa huệ", "The Persistence Of Memory"]
        self.ui.pushButton.clicked.connect(self.update_result)
        self.ui.toolButton.clicked.connect(self.next_slide)
        self.ui.toolButton_3.clicked.connect(self.previous_slide)
        self.ui.toolButton_2.clicked.connect(self.next_slide)
        self.ui.toolButton_7.clicked.connect(self.previous_slide)
        self.ui.toolButton_4.clicked.connect(self.next_slide)
        self.ui.toolButton_8.clicked.connect(self.previous_slide)
        self.ui.toolButton_5.clicked.connect(self.next_slide)
        self.ui.toolButton_9.clicked.connect(self.previous_slide)
        self.ui.toolButton_6.clicked.connect(self.next_slide)
        self.ui.toolButton_10.clicked.connect(self.previous_slide)
        self.ui.checkBox_10.clicked.connect(self.toggle_music)
        self.ui.checkBox_6.clicked.connect(self.toggle_music)
        self.ui.checkBox_7.clicked.connect(self.toggle_music)
        self.ui.checkBox_8.clicked.connect(self.toggle_music)
        self.ui.checkBox_9.clicked.connect(self.toggle_music)
    def next_slide(self):
        current_index = self.currentIndex()
        new_index = (current_index + 1) % self.count()
        self.setCurrentIndex(new_index)
    def previous_slide(self):
        current_index = self.currentIndex()
        new_index = (current_index - 1) % self.count()
        self.setCurrentIndex(new_index)

    def update_result(self):
        if self.ui.radioButton.isChecked():
            self.votes[0] += 1
        elif self.ui.radioButton_2.isChecked():
            self.votes[1] += 1
        elif self.ui.radioButton_3.isChecked():
            self.votes[2] += 1
        total_votes = sum(self.votes)
        self.ui.lineEdit.setText(str(total_votes))
        max_votes = max(self.votes)
        if max_votes > 0:
            max_index = self.votes.index(max_votes)
            winner = self.painting_names[max_index]
        else:
            winner = "No votes yet"

        self.ui.lineEdit_2.setText(winner)
    def reset_votes(self):
        self.votes = [0, 0, 0]
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)

    def toggle_music(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

