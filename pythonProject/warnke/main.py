import sys
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QMainWindow
import exercise3

app = QApplication(sys.argv)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PTTP")
        button = QPushButton("start")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def button_clicked(self):
        print('clicked')
window = MainWindow()
window.show()


app.exec()


