import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Inicjalizacja interfejsu użytkownika
        self.init_ui()

    def init_ui(self):
        # Tworzenie aplikacji Qt
        self.app = QApplication(sys.argv)

        # Tworzenie głównego okna
        self.window = QWidget()
        self.window.setWindowTitle(f"Person Info: {self.name}")
        self.window.setGeometry(100, 100, 300, 150)

        # Tworzenie layoutu
        layout = QVBoxLayout()

        # Dodawanie Combobox
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(self.comboBox)

        # Dodawanie przycisku "Introduce"
        self.introduce_button = QPushButton("Introduce")
        self.introduce_button.clicked.connect(self.introduce)
        layout.addWidget(self.introduce_button)

        # Dodawanie przycisku "Celebrate Birthday"
        self.birthday_button = QPushButton("Celebrate Birthday")
        self.birthday_button.clicked.connect(self.celebrate_birthday)
        layout.addWidget(self.birthday_button)

        # Ustawianie layoutu w oknie
        self.window.setLayout(layout)

    def show_ui(self):
        # Wyświetlanie okna
        self.window.show()

        # Uruchomienie pętli zdarzeń
        sys.exit(self.app.exec())

    def introduce(self):
        selected_option = self.comboBox.currentText()
        print(f"Selected Option: {selected_option}")
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday! Now I am {self.age} years old.")

# Utworzenie instancji klasy Person
person1 = Person("John Doe", 30)

# Wyświetlenie interfejsu użytkownika
person1.show_ui()
