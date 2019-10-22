# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datamaker.ui'
#
# Created by: PyQt5 UI code generator 5.13.0

import data_handler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTransform


class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(300, 300)
        self.setPixmap(pixmap)
        self.clearCanvas()

        self.last_x, self.last_y = None, None
        self.count = data_handler.findFinalNumber("../data/")

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(20)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def clearCanvas(self):
        painter = QtGui.QPainter(self.pixmap())
        pen = painter.pen()
        pen.setWidth(10)
        pen.setColor(Qt.white)
        painter.setPen(pen)

        brush = painter.brush()
        brush.setColor(Qt.white)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        painter.drawRect(0, 0, 300, 300)
        painter.end()
        self.update()
    
    def saveCanvas(self, fileName, options):
        self.stack = []
        if fileName == "":
            return
        srcImg = self.pixmap()
        srcImg = srcImg.toImage()
        srcImg = srcImg.scaledToWidth(28)
        srcImg = srcImg.scaledToHeight(28)

        if 1 in options and 2 not in options:
            for angle in [90, 180, 270]:
                img = srcImg.copy()
                tr = QTransform()
                tr.rotate(angle)
                img = img.transformed(tr)
                self.saveFile(fileName, img)
        elif 2 in options and 1 not in options:
            for angle in [180]:
                img = srcImg.copy()
                tr = QTransform()
                tr.rotate(angle)
                img = img.transformed(tr)
                self.saveFile(fileName, img)
        if 3 in options:
            img = srcImg.copy()
            tr = QTransform()
            tr.scale(-1, 1)
            img = img.transformed(tr)
            self.saveFile(fileName, img)
        if 4 in options:
            img = srcImg.copy()
            tr = QTransform()
            tr.scale(1, -1)
            img = img.transformed(tr)
            self.saveFile(fileName, img)
        if 5 in options:
            for xshift in [5, 10, 15, 20]:
                img = srcImg.copy()
                temp = img.copy(QtCore.QRect(0, 0, 30, 30))

                painter = QtGui.QPainter(img)
                pen = painter.pen()
                pen.setWidth(10)
                pen.setColor(Qt.white)
                painter.setPen(pen)

                brush = painter.brush()
                brush.setColor(Qt.white)
                brush.setStyle(Qt.SolidPattern)
                painter.setBrush(brush)

                painter.drawRect(0, 0, 30, 30)

                painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)
                painter.drawImage(QtCore.QRect(xshift, 0, 25, 30), temp, QtCore.QRect(0, 0, 25, 30))
                painter.end()
                self.saveFile(fileName, img)
        if 6 in options:
            for yshift in [5, 10, 15, 20]:
                img = srcImg.copy()
                temp = img.copy(QtCore.QRect(0, 0, 30, 30))

                painter = QtGui.QPainter(img)
                pen = painter.pen()
                pen.setWidth(10)
                pen.setColor(Qt.white)
                painter.setPen(pen)

                brush = painter.brush()
                brush.setColor(Qt.white)
                brush.setStyle(Qt.SolidPattern)
                painter.setBrush(brush)

                painter.drawRect(0, 0, 30, 30)

                painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)
                painter.drawImage(QtCore.QRect(0, yshift, 25, 30), temp, QtCore.QRect(0, 0, 25, 30))
                painter.end()
                self.saveFile(fileName, img)

        self.saveFile(fileName, srcImg)

    def saveFile(self, fileName, img):
        self.count[fileName] += 1
        
        name = "../data/" + fileName + "_" + str(self.count[fileName]) + ".png"
        self.stack.append(name)
        if not(img.save(name)):
            print("Error while saving")

    def undoSave(self):
        try:
            data_handler.undo(self.stack)
        except:
            pass
        self.stack = []


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.checked = []
        self.canvas = Canvas()
        self.yshift = 120

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.move(200, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.fileName = QtWidgets.QTextEdit(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(90, 50 + self.yshift, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fileName.setFont(font)
        self.fileName.setObjectName("fileName")

        self.flabel = QtWidgets.QLabel(self.centralwidget)
        self.flabel.setGeometry(QtCore.QRect(10, 50 + self.yshift, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flabel.setFont(font)
        self.flabel.setObjectName("flabel")

        self.counts = QtWidgets.QLabel(self.centralwidget)
        self.counts.setGeometry(QtCore.QRect(10, 350 + self.yshift, 790, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.counts.setFont(font)
        self.counts.setObjectName("counts")

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(615, 80 + self.yshift, 120, 40))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.pressed.connect(self.checkBoxes)
        self.saveButton.pressed.connect(lambda: self.canvas.saveCanvas(self.fileName.toPlainText(), self.checked))

        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(615, 130 + self.yshift, 120, 40))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.pressed.connect(self.canvas.clearCanvas)

        self.dupesButton = QtWidgets.QPushButton(self.centralwidget)
        self.dupesButton.setGeometry(QtCore.QRect(615, 180 + self.yshift, 120, 40))
        self.dupesButton.setObjectName("dupesButton")
        self.dupesButton.pressed.connect(self.canvas.clearCanvas)
        self.dupesButton.pressed.connect(lambda: data_handler.clear_dupes("../data/"))

        self.undoButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoButton.setGeometry(QtCore.QRect(615, 230 + self.yshift, 120, 40))
        self.undoButton.setObjectName("undoButton")
        self.undoButton.pressed.connect(self.canvas.clearCanvas)
        self.undoButton.pressed.connect(self.canvas.undoSave)

        self.countButton = QtWidgets.QPushButton(self.centralwidget)
        self.countButton.setGeometry(QtCore.QRect(615, 280 + self.yshift, 120, 40))
        self.countButton.setObjectName("countButton")
        self.countButton.pressed.connect(self.canvas.clearCanvas)
        self.countButton.pressed.connect(self.displayCount)

        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(10, 130 + self.yshift, 291, 22))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 160 + self.yshift, 291, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 190 + self.yshift, 291, 22))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 220 + self.yshift, 291, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 250 + self.yshift, 291, 22))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 280 + self.yshift, 291, 22))
        self.checkBox_6.setObjectName("checkBox_6")

        self.paintContainer = QtWidgets.QWidget(self.centralwidget)
        self.paintContainer.setGeometry(QtCore.QRect(250, 20 + self.yshift, 300, 300))
        self.paintContainer.setObjectName("paintContainer")

        w = QtWidgets.QWidget(self.paintContainer)
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        font = QtGui.QFont()
        font.setPointSize(25)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(255, 40, 300, 30))
        self.title.setFont(font)
        self.title.setText("Dataset Maker v1.0")
        self.title.setObjectName("title")

        font = QtGui.QFont()
        font.setPointSize(8)
        self.by = QtWidgets.QLabel(self.centralwidget)
        self.by.setGeometry(QtCore.QRect(500, 70, 300, 50))
        self.by.setFont(font)
        self.by.setText("~Github user: jerilMJ")

        font = QtGui.QFont()
        font.setPointSize(10)
        self.note = QtWidgets.QLabel(self.centralwidget)
        self.note.setGeometry(QtCore.QRect(0, 500, 800, 150))
        self.note.setFont(font)
        self.note.setText('''
        Note: 
        ----------
        * Images are saved under the name <label>_<number> to /data/.
        * Configure source code to change this.
        * Get source code at: 
        * 1st and 2nd options together are incompatible.
        ''')
        self.note.setObjectName("note")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dataset Maker"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.dupesButton.setText(_translate("MainWindow", "Eliminate dupes"))
        self.undoButton.setText(_translate("MainWindow", "Undo last save"))
        self.countButton.setText(_translate("MainWindow", "Count labels"))
        self.checkBox_1.setText(_translate("MainWindow", "Save 90, 180 and 270 degs"))
        self.checkBox_2.setText(_translate("MainWindow", "Save 180 deg"))
        self.checkBox_3.setText(_translate("MainWindow", "Flip vertically and save"))
        self.checkBox_4.setText(_translate("MainWindow", "Flip horizontally and save"))
        self.checkBox_5.setText(_translate("MainWindow", "Translate (r5-20) and save"))
        self.checkBox_6.setText(_translate("MainWindow", "Translate (d5-20) and save"))
        self.flabel.setText(_translate("MainWindow", "Enter label:"))

    def checkBoxes(self):
        self.checked = []
        if self.checkBox_1.checkState():
            self.checked.append(1)
        if self.checkBox_2.checkState():
            self.checked.append(2)
        if self.checkBox_3.checkState():
            self.checked.append(3)
        if self.checkBox_4.checkState():
            self.checked.append(4)
        if self.checkBox_5.checkState():
            self.checked.append(5)
        if self.checkBox_6.checkState():
            self.checked.append(6)

    def displayCount(self):
        count = data_handler.countFiles("../data/")
        msg = str(count)
        msg = msg.replace('defaultdict', '')
        msg = msg.replace('(', '')
        msg = msg.replace(')', '')
        msg = msg.replace('{', '')
        msg = msg.replace('}', '')
        msg = msg.replace("<class 'int'>, ", '')
        msg = msg.replace("'", '')
        self.counts.setText(msg)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet('''
    QMainWindow { 
        background: rgba(39, 39, 39, 150); 
    }
    QLabel#note { 
        background: rgba(56, 61, 57, 50); 
        color: 'white';
    }
    QLabel#title {
        color: rgba(75, 87, 201, 200);
    }
    QLabel#counts { 
        color: rgba(75, 87, 201, 200);
    }
    ''')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
