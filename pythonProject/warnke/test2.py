import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QTimer
import pygame
from threading import Thread
import time

class PygameThread(Thread):
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Tu obliczaj wartość swojej zmiennej
            value = 42

            # Przekazuj wartość do interfejsu PyQt6
            window.update_value.emit(value)

            clock.tick(60)
        pygame.quit()

class MyWindow(QMainWindow):
    update_value = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.update_value.connect(self.update_label)

    def update_label(self, value):
        self.label.setText(f"Wartość z Pygame: {value}")

def run_pygame():
    pygame_thread = PygameThread()
    pygame_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    QTimer.singleShot(0, run_pygame)  # Uruchomienie Pygame po uruchomieniu aplikacji

    sys.exit(app.exec())
