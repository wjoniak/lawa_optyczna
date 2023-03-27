import sys
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QPushButton,QSlider,QLabel
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout,QGraphicsItem
from PyQt6.QtGui import QPalette, QColor,QPen,QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    x = 200
    h = 50
    h1 = 50
    f1 = 100
    f2 = 100
    y = 200

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()




        self.construct = self.draw()
        self.layout1.addWidget(self.construct)
        self.layout1.addLayout(layout2)

        f = QSlider(Qt.Orientation.Horizontal)
        f.setRange(50, 250)
        f.valueChanged.connect(self.move_f)
        layout2.addWidget(QLabel("ogniskowa(f): "))
        layout2.addWidget(f)

        slider_x = QSlider(Qt.Orientation.Horizontal)
        slider_x.setRange(30, 300)
        slider_x.valueChanged.connect(self.move_x)
        layout2.addWidget(QLabel("odległosć przedmiotu(x): "))
        layout2.addWidget(slider_x)

        slider_y = QSlider(Qt.Orientation.Horizontal)
        slider_y.setRange(20, 100)

        slider_y.valueChanged.connect(self.move_y)
        layout2.addWidget(QLabel("wysokosć przedmiotu(h): "))
        layout2.addWidget(slider_y)

        layout2.addWidget(QPushButton("start"))

        widget = QWidget()
        widget.setLayout(self.layout1)
        self.setCentralWidget(widget)

    def update(self):
        if(self.x != self.f2):
            self.y = int((self.x * self.f2) / (self.x - self.f2))
        if self.x != 0:
            self.h1 = int((self.y * self.h) / self.x)
        print(self.f1,self.f2,self.x, self.h, self.y, self.h1)
        self.point_y.setX(self.y - 200)
        self.point_y.setY(self.h1-50)
        self.point_x.setX(200 - self.x)
        self.point_x.setY( -self.h +150)
        self.point_f_left.setX( -self.f1 + 100)
        self.point_f_right.setX( self.f2 - 100)

        self.ray2.setLine(400 - self.x,200 - self.h, 400 + self.y, self.h1 + 200)
        self.ray1a.setLine(400 - self.x,200 - self.h, 400,200 - self.h)
        self.ray1b.setLine(400, 200 - self.h, 400 + self.y, self.h1 + 200)

    def  move_f(self,value):
        self.f1 =  value
        self.f2 =  value
        self.update()



    def move_x(self, value):
        self.x = value
        self.update()

    def move_y(self, value):
        self.h = value
        self.update()



    def draw(self):
        self.scene = QGraphicsScene(0, 0, 800, 400)
        self.scene.setBackgroundBrush(QColor(200, 200, 200))

        pen = QPen()
        pen1 = QPen()
        pen2 = QPen()
        pen.setWidth(4)
        pen1.setColor(QColor(200,0,0))
        pen1.setWidth(4)
        pen2.setColor(QColor(0, 200, 0))
        pen2.setWidth(4)

        self.scene.addLine(20, 200, 780, 200, pen)
        self.scene.addLine(400, 20, 400, 380, pen)
        self.scene.addLine(400, 20, 405, 40, pen)
        self.scene.addLine(400, 20, 395, 40, pen)
        self.scene.addLine(400, 380, 405, 360, pen)
        self.scene.addLine(400, 380, 395, 360, pen)

        # lewe ognisko soczewki
        self.point_f_left = self.scene.addEllipse(400 - self.f1, 197, 6, 6, pen)
        self.text_f_left = self.scene.addText("F")
        self.text_f_left.setPos(400 - self.f1, 170)

        # prawe ognisko soczewki
        self.point_f_right = self.scene.addEllipse(400 + self.f2, 197, 6, 6, pen)
        self.text_f_right = self.scene.addText("F")
        self.text_f_right.setPos(400 + self.f2, 170)

        # przedmiot
        self.point_x = self.scene.addEllipse(400 - self.x, self.h, 6, 6, pen1)
        self.text_x = self.scene.addText("A")
        self.text_x.setPos(400 - self.x, self.h)

        # obraz
        self.point_y = self.scene.addEllipse(400 + self.y, 200 + self.h1, 6, 6, pen2)
        self.text_y = self.scene.addText("A'")
        self.text_y.setPos(400 + self.y, 200 + self.h)

        #promień 1
        self.ray1a =self.scene.addLine(400 - self.x ,200 -self.h, 400, 200 - self.h)
        self.ray1b = self.scene.addLine(400 , 200 - self.h, 400 + self.y, 200 + self.h)
        # promień 2
        self.ray2 = self.scene.addLine(400 - self.x, 200 - self.h, 400+self.y, 200 + self.h1)
        return QGraphicsView(self.scene)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

