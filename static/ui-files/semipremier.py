from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


def verif(text):
    return text.isnumeric() and int(text) > 2


def premier(n):
    s = 0
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            s = s + 1
    return s == 0


def semipremier(n):
    for i in range(2, int(n / 2) + 1):
        if premier(i) and n % i == 0 and premier(n // i):
            return True
    return False


def Play():
    text = fen.lineEdit.text()
    if (verif(text)):
        if (semipremier(int(text))):
            fen.label_3.setText(f" {text} est un nombre semi-premier ")
        else:
            fen.label_3.setText(f" {text} n'est pas un nombre semi-premier ")

    else:
        fen.label_3.setText("Entrer un nombre valide !")
        fen.lineEdit.clear()


app = QApplication([])

fen = loadUi("semipremier.ui")

fen.pushButton.clicked.connect(Play)

fen.show()

app.exec()
