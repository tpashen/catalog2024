from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap 
from PyQt5 import QtGui

app = QApplication([])
win=QWidget()
win.resize(700,500)
win.setWindowTitle('Cat')
win.show()

label_p=QLabel('')
label_p.hide()
pixmapimage = QPixmap('1.jpg')
w, h = label_p.width(), label_p.height()
pixmapimage = pixmapimage.scaled(200, 200, Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

w=QVBoxLayout()
w.addWidget(label_p)
win.setLayout(w)

app.exec()