from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    turn = 0

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(544, 445)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        Window.setFont(font)
        self.btn1 = QtWidgets.QPushButton(Window)
        self.btn1.setGeometry(QtCore.QRect(80, 100, 91, 81))
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(Window)
        self.btn2.setGeometry(QtCore.QRect(190, 100, 91, 81))
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(Window)
        self.btn3.setGeometry(QtCore.QRect(300, 100, 91, 81))
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.btn5 = QtWidgets.QPushButton(Window)
        self.btn5.setGeometry(QtCore.QRect(190, 200, 91, 81))
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(Window)
        self.btn6.setGeometry(QtCore.QRect(300, 200, 91, 81))
        self.btn6.setText("")
        self.btn6.setObjectName("btn6")
        self.btn4 = QtWidgets.QPushButton(Window)
        self.btn4.setGeometry(QtCore.QRect(80, 200, 91, 81))
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.btn8 = QtWidgets.QPushButton(Window)
        self.btn8.setGeometry(QtCore.QRect(190, 300, 91, 81))
        self.btn8.setText("")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(Window)
        self.btn9.setGeometry(QtCore.QRect(300, 300, 91, 81))
        self.btn9.setText("")
        self.btn9.setObjectName("btn9")
        self.btn7 = QtWidgets.QPushButton(Window)
        self.btn7.setGeometry(QtCore.QRect(80, 300, 91, 81))
        self.btn7.setText("")
        self.btn7.setObjectName("btn7")
        self.scoreY = QtWidgets.QLabel(Window)
        self.scoreY.setGeometry(QtCore.QRect(420, 160, 91, 41))
        self.scoreY.setObjectName("scoreY")
        self.scoreX = QtWidgets.QLabel(Window)
        self.scoreX.setGeometry(QtCore.QRect(420, 110, 101, 41))
        self.scoreX.setObjectName("scoreX")
        self.startBtn = QtWidgets.QPushButton(Window)
        self.startBtn.setGeometry(QtCore.QRect(410, 320, 111, 41))
        self.startBtn.setObjectName("startBtn")
        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(90, 50, 221, 31))
        self.label.setObjectName("label")

        self.btn1.clicked.connect(lambda: self.bosildi(self.btn1))
        self.btn2.clicked.connect(lambda: self.bosildi(self.btn2))
        self.btn3.clicked.connect(lambda: self.bosildi(self.btn3))
        self.btn4.clicked.connect(lambda: self.bosildi(self.btn4))
        self.btn5.clicked.connect(lambda: self.bosildi(self.btn5))
        self.btn6.clicked.connect(lambda: self.bosildi(self.btn6))
        self.btn7.clicked.connect(lambda: self.bosildi(self.btn7))
        self.btn8.clicked.connect(lambda: self.bosildi(self.btn8))
        self.btn9.clicked.connect(lambda: self.bosildi(self.btn9))

        self.startBtn.clicked.connect(self.startGame)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


    def startGame(self):
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(True)
        self.btn3.setEnabled(True)
        self.btn4.setEnabled(True)
        self.btn5.setEnabled(True)
        self.btn6.setEnabled(True)
        self.btn7.setEnabled(True)
        self.btn8.setEnabled(True)
        self.btn9.setEnabled(True)

        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.label.setText("Turn: X")

        self.btn1.setStyleSheet("border: 3px solid grey;")
        self.btn2.setStyleSheet("border: 3px solid grey;")
        self.btn3.setStyleSheet("border: 3px solid grey;")
        self.btn4.setStyleSheet("border: 3px solid grey;")
        self.btn5.setStyleSheet("border: 3px solid grey;")
        self.btn6.setStyleSheet("border: 3px solid grey;")
        self.btn7.setStyleSheet("border: 3px solid grey;")
        self.btn8.setStyleSheet("border: 3px solid grey;")
        self.btn9.setStyleSheet("border: 3px solid grey;")
        
        self.label.setText("Turn: " + ("X" if not self.turn % 2 else "O"))

        self.turn = 0


    def bosildi(self, btn: QtWidgets.QPushButton):
        btn.setText("X" if not self.turn % 2 else "O")
        btn.setEnabled(False)
        if not self.turn%2:
            self.label.setText("Turn: 0")
        else:
            self.label.setText("Turn: X")
        
        btn.setStyleSheet("font-size:25px;")
        
        if self.tekshir():
            if not self.turn % 2:
                self.label.setText("X yutti")
                self.scoreX.setText("X: " + str(int(self.scoreX.text().split(": ")[1]) + 1))
            else:
                self.label.setText("0 yutti")
                self.scoreY.setText("O: " + str(int(self.scoreY.text().split(": ")[1]) + 1))
            self.tozalash()
            return
        self.turn += 1

        if self.turn == 9:
            self.label.setText("Durrang")
            self.btn1.setStyleSheet("border: 3px solid red;")
            self.btn2.setStyleSheet("border: 3px solid red;")
            self.btn3.setStyleSheet("border: 3px solid red;")
            self.btn4.setStyleSheet("border: 3px solid red;")
            self.btn5.setStyleSheet("border: 3px solid red;")
            self.btn6.setStyleSheet("border: 3px solid red;")
            self.btn7.setStyleSheet("border: 3px solid red;")
            self.btn8.setStyleSheet("border: 3px solid red;")
            self.btn9.setStyleSheet("border: 3px solid red;")
            
            self.label.adjustSize()

    
    def tekshir(self) -> bool:
        txt1 = self.btn1.text()
        txt2 = self.btn2.text()
        txt3 = self.btn3.text()
        txt4 = self.btn4.text()
        txt5 = self.btn5.text()
        txt6 = self.btn6.text()
        txt7 = self.btn7.text()
        txt8 = self.btn8.text()
        txt9 = self.btn9.text()
        if txt1 == txt2 and txt2 == txt3 and txt1 != "":
            self.btn1.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn2.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn3.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt4 == txt5 and txt5 == txt6 and txt6 != "":
            self.btn4.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn5.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn6.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt7 == txt8 and txt8 == txt9 and txt9 != "":
            self.btn7.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn8.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn9.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt1 == txt4 and txt4 == txt7 and txt1 != "":
            self.btn1.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn4.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn7.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt2 == txt5 and txt5 == txt8 and txt2 != "":
            self.btn2.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn5.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn8.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt3 == txt6 and txt6 == txt9 and txt3 != "":
            self.btn3.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn6.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn9.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt1 == txt5 and txt5 == txt9 and txt1 != "":
            self.btn1.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn5.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn9.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
        if txt3 == txt5 and txt5 == txt7 and txt3 != "":
            self.btn3.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn5.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            self.btn7.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border: 3px solid green;
                border-radius: 20px;
                }
            """)
            return True
            
        return False


    def tozalash(self):
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn5.setEnabled(False)
        self.btn6.setEnabled(False)
        self.btn7.setEnabled(False)
        self.btn8.setEnabled(False)
        self.btn9.setEnabled(False)
        self.startBtn.setText("Restart")


    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Game"))
        self.scoreY.setText(_translate("Window", "O: 0"))
        self.scoreX.setText(_translate("Window", "X: 0"))
        self.startBtn.setText(_translate("Window", "start"))
        self.label.setText(_translate("Window", "Turn: X"))


if __name__ == "__main__":
    import sys
    import os
    os.system("cls")
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
