import sys

import pygame
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QMainWindow,QHBoxLayout,QVBoxLayout,QComboBox
import exercise3

app = QApplication(sys.argv)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = 1
        self.setWindowTitle("PTTP")
        self.game_selector = QComboBox()
        self.game_selector.addItem("postrzeganie kierunkowe -  wzrok i słuch")
        self.game_selector.addItem("postrzeganie kierunkowe - tylko słuch")
        self.game_selector.addItem("postrzeganie kierunkowe - tylko wzrok")
        self.game_selector.currentIndexChanged.connect(self.selectiongame)
        self.button_start = QPushButton("start")
        #button_start.setCheckable(True)
        self.button_start.clicked.connect(self.start_game)
        self.button_stop = QPushButton("stop")
        self.button_stop.setEnabled(False)


        self.button_stop.clicked.connect(self.stop_game)
        layout = QHBoxLayout()
        layout.addWidget(self.game_selector)
        layout.addWidget(self.button_start)
        layout.addWidget(self.button_stop)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def start_game(self):

        self.button_stop.setEnabled(True)
        result = exercise3.exercise(self.game)

        exercise3.wynik(result)
    def stop_game(self):
        self.button_stop.setEnabled(False)
        pygame.display.quit()

    def selectiongame(self, i):
        print (i)
        self.game = i+1

window = MainWindow()

app.setStyleSheet("""
    QWidget {
        background-color: "green";
        color: "white";
        font-size: 16px;
    }
    QPushButton {
        font-size: 16px;
        background-color: "darkgreen";
        padding:6px;
    }
    QComboBox {
        background-color: "green";
        color: "white";
        padding:8px;
    }
""")
window.show()


app.exec()


