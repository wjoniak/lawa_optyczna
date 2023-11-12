import sys

import pygame
from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QMainWindow,QHBoxLayout,\
    QVBoxLayout,QComboBox,QLabel,QFormLayout,QSpinBox,QLineEdit
import exercise3

app = QApplication(sys.argv)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = 1
        self.setGeometry(50, 50,600,600)
        self.setWindowTitle("PTTP")

        self.client_selector = QComboBox()
        self.client_selector.addItem("Jan Nowak")
        self.client_selector.addItem("Tadeusz Kowalski")
        self.client_selector.addItem("Martyna Jankowska")


        self.game_selector = QComboBox()
        #self.game_selector.addItem("postrzeganie kierunkowe -  wzrok i słuch")
        #self.game_selector.addItem("postrzeganie kierunkowe - tylko słuch")
        #self.game_selector.addItem("postrzeganie kierunkowe - tylko wzrok")
        self.game_selector.addItem("wybierz ćwiczenie...")
        self.game_selector.addItem("1: Próg kolejności wzrokowej")
        self.game_selector.addItem("2: Próg kolejności słuchowej")
        self.game_selector.addItem("3: Słyszenie kierunkowe")
        self.game_selector.addItem("4: Różnicowane tonów")
        self.game_selector.addItem("5: Synchroniczne wystukiwanie rytmu")
        self.game_selector.addItem("6: Czas reakcji z wyborem")
        self.game_selector.addItem("7: Rozpoznawanie wzorca częstotliwości czasu")
        self.game_selector.addItem("8: Koordynacja oko-ręka")
        self.game_selector.addItem("9: Czytanie pseudotekstów")
        self.game_selector.addItem("10: Zdolność do krótkotrwałego zapamiętywania sylab")
        self.game_selector.addItem("11: Selektywność percepcji")
        self.game_selector.addItem("12: Spostrzeganie dynamiczne")
        self.game_selector.addItem("13: Współpraca obuoczna")
        self.game_selector.addItem("14: Literowanie wzrokowe")

        self.game_selector.currentIndexChanged.connect(self.selectiongame)

        self.opis = QLabel(self)  # Zmiana na QLabel
        self.opis.setWordWrap(True)  # Ustawienie zawijania tekstu


        self.game_selector.currentIndexChanged.connect(self.selectiongame)
        self.button_start = QPushButton("start")
        self.button_start.clicked.connect(self.start_game)

        layout_V = QVBoxLayout()
        layout_H = QHBoxLayout()

        layout_V.addWidget(self.game_selector)

        layout_V.addWidget(self.opis)

        layout_V.addWidget(self.client_selector)
        layout_V.addWidget(self.settings(1))
        layout_V.addWidget(self.button_start)

        widget = QWidget()
        widget.setLayout(layout_V)
        self.setCentralWidget(widget)



    def start_game(self):

        result = exercise3.exercise(self.game)
        exercise3.wynik(result)

    def settings(self,game):
        form = QWidget()
        layout = QFormLayout()

        # Dodawanie pierwszego wiersza z QSpinBox
        spinbox1 = QLineEdit()
        spinbox1.setText('100')
        layout.addRow("czas treningu:", spinbox1)

        # Dodawanie drugiego wiersza z QSpinBox
        spinbox2 = QLineEdit()

        layout.addRow(" startowy poziom trudności:", spinbox2)



        # Ustawianie układu
        form.setLayout(layout)
        return form


    def selectiongame(self, i):
        self.game = i
        if self.game == 1:
            self.opis.setText("Umiejętność porządkowania dwóch następujących po sobie szybko bodźców wzrokowych. Wydłużony próg kolejności wzrokowej powoduje, że zazwyczaj szybkie skanowanie wzrokowe obrazów – potrzebne przy czytaniu – przebiega o wiele wolniej i staje się zajęciem pracochłonnym. Próg kolejności wzrokowej mierzony jest za pomocą następujących bezpośrednio po sobie błysków. Pacjent proszony jest o wskazanie ich kolejności.")
        elif self.game == 2:
            self.opis.setText("Wielkość określająca rozdzielczość czasową bodźców słuchowych, (odległość między dwoma takimi bodźcami). Zbyt wysoki próg kolejności słuchowej sprawia, że dziecko z trudnością odróżnia od siebie głoski zwarto-wybuchowe (b-d-g-k-p-t), co prowadzi do trudności w zrozumieniu mowy.Próg kolejności słuchowej mierzy się za pomocą następujących bezpośrednio po sobie dźwięków. Osoba wskazuje, który dźwięk pojawił się w słuchawkach jako pierwszy.")
        elif self.game == 3:
            self.opis.setText("Umiejętność lokalizacji źródła dźwięku, pozwala na śledzenie toku lekcji w otoczeniu dźwięków zakłócających, które w standardowym pomieszczeniu klasowym mają natężenie ok. 50–60 dB(A). \nSłyszenie kierunkowe mierzone jest za pomocą bocznego kliknięcia w słuchawkach. Pacjent proszony jest o wskazanie kierunku, z którego pojawiło się kliknięcie.")
        elif self.game == 4:
            self.opis.setText("Umiejętność szybkiego spostrzegania różnic wysokości dźwięków pojawiających się jeden po drugim. Zdolność ta jest niezwykle istotna dla różnicowania samogłosek i dekodowania melodii mówienia. \nRóżnicowanie tonów mierzy się za pomocą dwóch różnych tonów pojawiających się w słuchawkach. Należy określić kolejność słyszanego niskiego dźwięku.")
        elif self.game == 5:
            self.opis.setText("Umiejętność przełożenia zmieniających się kliknięć słyszanych raz z lewej, raz z prawej strony na odpowiednie stukanie dłońmi.\nZdolność ta świadczy o efektywnej koordynacji półkul mózgowych, która nie działa prawidłowo u osób z dysleksją, z zaburzeniami przetwarzania słuchowego.\nPacjent proszony jest o naciskanie przycisków w rytm kliknięć (stosownie do nich), na zmianę pojawiających się w słuchawkach raz z prawej raz z lewej strony.")
        elif self.game == 6:
            self.opis.setText("Jest to umiejętność szybkiej i trafnej reakcji motorycznej przy wyborze jednej z wielu możliwości.\nDzieci dyslektyczne przy wykonywaniu zadań związanych z czasem reakcji z wyborem w przypadku kanału wzrokowo-motorycznego i słuchowo-motorycznego, osiągają znacznie gorsze wyniki. Umiejętność ta decyduje o czasie rozpoznawania fonemów i grafemów. \nCzas reakcji z wyborem ustala się mierząc czas, jaki upływa od momentu pojawienia się bodźca do wyboru – naciśnięcia przycisku na panelu odpowiedzi. Pacjent musi szybko reagować na niskie dżwięki, które pojawiają się naprzemiennie w słuchawkach.")
        elif self.game == 7:
            self.opis.setText("Rozpoznawanie wzorca częstotliwości i czasu to umiejętności ważne do segmentowania ciągłego potoku mowy przy rozpoznawaniu języka mówionego na poziomie niejęzykowym. Są istotne dla przekładania melodii mowy na informację. Testy mierzą umiejętność zlokalizowania tonu o odmiennej wysokości lub długości spośród trzech dźwięków.\nOsoba słyszy w słuchawkach ciąg trzech dźwięków: rozpoznaje i określa pozycję dźwięku odmiennego od dwóch pozostałych.")
        elif self.game == 8:
            self.opis.setText("Umiejętność polegająca na szybkiej korekcie motorycznej rozpoznawalnych wizualnie odchyleń drążka do balansowania.\nPacjent balansuje lekkim drążkiem na grzbiecie dłoni przez 10 sekund, starając się kontrolować i korygować swoje ruchy.")
        elif self.game == 9:
            self.opis.setText("Zadanie wykonuje się za pomocą czytania pseudotekstów – czyli specjalnie przygotowanych tekstów pozbawionych znaczenia. Test pozwala na rozpoznanie strategii czytania i stopnia zautomatyzowania podstawowej konwersji grafemów na fonemy.\nOsoby mające problemy z pisownią z różnych względów próbują rozpoznawać całe słowa po jego konturze, a nie po szczegółowej strukturze poszczególnych liter. W ten sposób nie powstają u nich zróżnicowane reprezentacje prawidłowej pisowni.\n Pacjent czyta psueudoteksty. Podczas zadania mierzona jest liczba błędów oraz czas potrzebny na wykonanie ćwiczenia.")
        elif self.game == 10:
            self.opis.setText("Umiejętność krótkotrwałego zapamiętywania sylab i słów w procesie czytania, jest istotna do czytania ze zrozumieniem. \n Krótkoterminowe zapamiętywanie mierzone jest przez powtarzanie ciągów sylab złożonych z od 2 do 6 elementów.")
        elif self.game == 11:
            self.opis.setText("Umiejętność opierająca się na funkcjach podstawowych, zwłaszcza zaś na przetwarzaniu czasowym. Selektywność percepcji jest niezbędna dla bezbłędnego rozróżniania głosek o podobnych brzmieniach, zwłaszcza głosek zwarto-wybuchowych, również na tle dźwięków zakłócających. \nSelektywność percepcji mierzy się z użyciem pseudosłów. Badany słyszy w słuchawkach tekst i powtarza na głos usłyszane słowa, które są następnie porównywane przez badającego z wynikami. ")
        elif self.game == 12:
            self.opis.setText("Umiejętność szybkiego i płynnego podążania obydwoma oczami za oglądanym przedmiotem. Jest to umiejętność istotna dla łatwości i szybkości czytania, obejmowania wzrokiem tekstu do przeczytania, ponieważ podczas procesu nie skanujemy jednej litery po drugiej.\n Test spostrzegania dynamicznego wykonuje się sprawdzając u dziecka płynne podążanie obydwoma oczami za tzw. obiektem fiksacji.")
        elif self.game == 13:
            self.opis.setText("Test widzenia stereoskopowego, który sprawdza zdolność widzenia w trzech wymiarach z bliskiej odległości. Jest to umiejętność ważna do niezakłóconego szybkiego czytania.\nPacjent patrzy na specjalnie zaprojektowane plansze z implementowanymi symbolami, kształtami. Zadaniem pacjenta jest wymienić wszystkie z czterech prezentowanych obrazków. W przypadku  błędnych odpowiedzi można domniewywać problemów w widzeniu stereoskopowym i zaleca się wykonanie dalszych badań w kierunku wykluczenia zeza ukrytego.")
        elif self.game == 14:
            self.opis.setText("Literowanie wzrokowe to warunek konieczny do opanowania prawidłowej pisowni. Ważna jest umiejętność przywołania słownictwa z naszego wewnętrznego wizualnego leksykonu.\nOsoba powinna potrafić przeliterować znane mu słowo zadane przez terapeutę zarówno od przodu, jak i od tyłu. Dzięki temu można ustalić, jaką technikę literowania lub głoskowania stosuje pacjent.")



window = MainWindow()
window.show()
with open("Adaptic.qss", "r") as file:
    app.setStyleSheet(file.read())
app.exec()


