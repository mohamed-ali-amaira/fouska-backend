from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from math import sqrt


def verif(text):
    return text.isnumeric() and int(text) > 1


def premier(n):
    c = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            c = c + 1
    return c == 0


def lisse(n):
    pgd = 1
    for i in range(2, n // 2 + 1):
        if (n % i == 0 and premier(i)):
            pgd = i
    return pgd <= sqrt(n)


def Play():
    text = fen.lineEdit.text()
    if (verif(text)):
        if (lisse(int(text))):
            fen.label_3.setText(f"{text} est un nombre lisse")
        else:
            fen.label_3.setText(f"{text} n'est pas un nombre lisse")
    else:
        fen.label_3.setText("Veillez introduire un nombre > 1")
        fen.lineEdit.clear()


app = QApplication([])

fen = loadUi("lisse.ui")

fen.pushButton.clicked.connect(Play)

fen.show()

app.exec()
