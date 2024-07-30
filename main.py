from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)

        self.label1 = QLabel("Ism: ")
        self.label1.setStyleSheet("font-size: 15px; color: blue")
        self.input1 = QLineEdit()
        self.input1.setStyleSheet("font-size: 15px")


        self.label2 = QLabel("Familiya: ")
        self.label2.setStyleSheet("font-size: 15px; color: blue")
        self.input2 = QLineEdit()
        self.input2.setStyleSheet("font-size: 15px")



        self.label3 = QLabel("Elektron pochta: ")
        self.label3.setStyleSheet("font-size: 15px; color: blue")
        self.input3 = QLineEdit()
        self.input3.setStyleSheet("font-size: 15px")



        self.label4 = QLabel("Parol: ")
        self.label4.setStyleSheet("font-size: 15px; color: blue")
        self.input4 = QLineEdit()
        self.input4.setStyleSheet("font-size: 15px")



        self.btn = QPushButton()
        self.btn.setText("Ro'yxatdan o'tish tugmasi")
        self.btn.setStyleSheet("font-size: 17px; color: blue; margin-top: 30px")
        self.btn.clicked.connect(self.show_malumotlar)


        layout1 = QHBoxLayout()
        layout1.addWidget(self.label1)
        layout1.addWidget(self.input1)


        layout2 = QHBoxLayout()
        layout2.addWidget(self.label2)
        layout2.addWidget(self.input2)


        layout3 = QHBoxLayout()
        layout3.addWidget(self.label3)
        layout3.addWidget(self.input3)


        layout4 = QHBoxLayout()
        layout4.addWidget(self.label4)
        layout4.addWidget(self.input4)


        layoutlar = QVBoxLayout()
        layoutlar.addLayout(layout1)
        layoutlar.addLayout(layout2)
        layoutlar.addLayout(layout3)
        layoutlar.addLayout(layout4)
        layoutlar.addWidget(self.btn)


        widget = QWidget()
        widget.setLayout(layoutlar)

        self.setCentralWidget(widget)

    def show_malumotlar(self):
        text1 = self.input1.text()
        text2 = self.input2.text()
        text3 = self.input3.text()
        text4 = self.input4.text()

        res = QMessageBox.question(self, "Malumotlar oynasi", "Malumotlarni to'gri kiritganizga aminmisiz", QMessageBox.Ok | QMessageBox.Cancel)
        if res == QMessageBox.Ok:
            print(f"Ism: {text1}\nFamiliya: {text2}\nElektron pochta: {text3}\nParol: {text4}")
        else:
            print("Siz malumotlarni xato kirittingiz!")


main = MainWindow()
main.show()

app.exec_()