from PyQt6.QtWidgets import *
from gui import *
from PyQt6.QtGui import QPixmap
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        qpixmap = QPixmap("Flag Banner.png")
        self.image_label.setPixmap(qpixmap)

        self.checkBox_john.toggle()

        self.submit_button.clicked.connect(lambda: self.submit())

    def submit(self):
        self.voterID = self.voterID_text.text().strip().lower()

        self.vote = "No Vote"

        if self.checkBox_john.isChecked() == True:
            self.vote = "John Smith"
        elif self.checkBox_jane.isChecked() == True:
            self.vote = "Jane Doe"
        elif self.checkBox_kyle.isChecked() == True:
            self.vote = "Kyle Snell"
        elif self.checkBox_bob.isChecked() == True:
            self.vote = "Bob McDonald"

        csv_file = open("Vote Database", "r")
        content = csv.reader(csv_file, delimiter = ",")

        copy = 0

        for line in content:
            if self.voterID in line:
                copy = 1

        if copy == 1:
            self.results_label.setText("Invalid VoterID!")
            csv_file.close()
        elif copy == 0:
            self.results_label.setText("")
            csv_file.close()
            csv_file2 = open("Vote Database", "a", newline='')
            contents = csv.writer(csv_file2)
            contents.writerow([self.voterID, self.vote])
            csv_file2.close()

        self.voterID_text.setText("")
