from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 621)
        MainWindow.setFixedSize(500, 621)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(150, 10, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")

        self.image_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(10, 0, 501, 221))
        self.image_label.setObjectName("image_label")

        self.voterID_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.voterID_label.setGeometry(QtCore.QRect(30, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.voterID_label.setFont(font)
        self.voterID_label.setObjectName("voterID_label")

        #Labels above

        self.voterID_text = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.voterID_text.setGeometry(QtCore.QRect(150, 230, 311, 41))
        self.voterID_text.setObjectName("voterID_text")

        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 290, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.candidates_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates_label.setGeometry(QtCore.QRect(160, 310, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.candidates_label.setFont(font)
        self.candidates_label.setObjectName("candidates_label")

        #Checkboxes below

        self.checkBox_john = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_john.setGeometry(QtCore.QRect(80, 360, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_john.setFont(font)
        self.checkBox_john.setObjectName("checkBox_john")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_john)

        self.checkBox_kyle = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_kyle.setGeometry(QtCore.QRect(80, 420, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_kyle.setFont(font)
        self.checkBox_kyle.setObjectName("checkBox_kyle")
        self.buttonGroup.addButton(self.checkBox_kyle)

        self.checkBox_jane = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_jane.setGeometry(QtCore.QRect(280, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_jane.setFont(font)
        self.checkBox_jane.setObjectName("checkBox_jane")
        self.buttonGroup.addButton(self.checkBox_jane)

        self.checkBox_bob = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_bob.setGeometry(QtCore.QRect(280, 420, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.checkBox_bob.setFont(font)
        self.checkBox_bob.setObjectName("checkBox_bob")
        self.buttonGroup.addButton(self.checkBox_bob)

        #The rest below

        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(40, 470, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")

        self.results_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.results_label.setGeometry(QtCore.QRect(50, 540, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.results_label.setFont(font)
        self.results_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.results_label.setObjectName("results_label")

        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 450, 461, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSCI 1620 Final Project 1"))
        self.title_label.setText(_translate("MainWindow", "2024 Voting Application"))
        self.image_label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/Flag Banner.png\"/></p></body></html>"))
        self.voterID_label.setText(_translate("MainWindow", "Voter ID:"))
        self.candidates_label.setText(_translate("MainWindow", "Candidates"))
        self.checkBox_john.setText(_translate("MainWindow", "John Smith"))
        self.checkBox_kyle.setText(_translate("MainWindow", "Kyle Snell"))
        self.checkBox_jane.setText(_translate("MainWindow", "Jane Doe"))
        self.checkBox_bob.setText(_translate("MainWindow", "Bob McDonald"))
        self.submit_button.setText(_translate("MainWindow", "Submit Vote"))
        self.results_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\"><br/></span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
