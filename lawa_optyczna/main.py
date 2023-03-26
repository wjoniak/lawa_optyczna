import sys
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QPushButton,QSlider,QLabel
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout,QGraphicsItem
from PyQt6.QtGui import QPalette, QColor,QPen,QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        self.scene = QGraphicsScene(0, 0, 800, 400)
        self.scene.setBackgroundBrush(QColor(200, 200, 200))

        pen = QPen()
        pen.setWidth(4)



        self.scene.addLine(20,200,780,200,pen)
        self.scene.addLine(400, 20, 400, 380,pen)
        self.scene.addLine(400, 20, 405, 40,pen)
        self.scene.addLine(400, 20, 395, 40,pen)
        self.scene.addLine(400, 380, 405, 360,pen)
        self.scene.addLine(400, 380, 395, 360,pen)
        #ognisko soczewki
        self.point_f = self.scene.addEllipse(50,197,6,6,pen)
        self.point_f.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        self.text_f = self.scene.addText("F")
        self.text_f.setPos(50,170)

        # przedmiot
        self.point_x = self.scene.addEllipse(20, 100, 6, 6, pen)
        self.point_x.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        self.text_x = self.scene.addText("A")
        self.text_x.setPos(15, 82)




        view = QGraphicsView(self.scene)
        layout1.addWidget(view)
        layout1.addLayout(layout2)

        f = QSlider(Qt.Orientation.Horizontal)
        f.setRange(0, 300)
        f.valueChanged.connect(self.move_f)
        layout2.addWidget(QLabel("ogniskowa(f): "))
        layout2.addWidget(f)

        x = QSlider(Qt.Orientation.Horizontal)
        x.setRange(0, 380)
        x.valueChanged.connect(self.move_x)
        layout2.addWidget(QLabel("odległosć przedmiotu(x): "))
        layout2.addWidget(x)

        y = QSlider(Qt.Orientation.Horizontal)
        y.setRange(20, 350)
        y.setValue(100)
        y.valueChanged.connect(self.move_y)
        layout2.addWidget(QLabel("wysokosć przedmiotu(h): "))
        layout2.addWidget(y)

        layout2.addWidget(QPushButton("start"))

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def  move_f(self,value):
        self.point_f.setX(value)
        self.text_f.setX(value+50)


    def move_x(self, value):
        self.point_x.setX(value)
        self.text_x.setX(value)

    def move_y(self, value):
        self.point_x.setY(value-50)
        self.text_x.setY(value-50)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
