from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


def verif(text):
    return text.isnumeric() and int(text) > 2 and int(text) < 1000


def somme(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    return s


def facteurs(n):
    s = 0
    i = 2
    while (n != 1):
        if (n % i == 0):
            n = n // i
            s += somme(str(i))
        else:
            i += 1
    return s


def smith(n):
    s = facteurs(int(n))
    s2 = somme(n)
    return s == s2


def Play():
    text = fen.lineEdit.text()
    if (verif(text)):
        if smith((text)):
            fen.label_5.setText(f"{text} est un nombre smith")

        else:
            fen.label_5.setText(f"{text} n'est pas un nombre smith")

    else:
        fen.label_5.setText("Entrer un entier valide")
        fen.lineEdit.clear()


def annuler():
    fen.lineEdit.clear()


def quitter():
    fen.close()


app = QApplication([])

fen = loadUi("smith.ui")

fen.pushButton.clicked.connect(Play)
fen.pushButton_2.clicked.connect(annuler)
fen.pushButton_3.clicked.connect(quitter)


fen.show()

app.exec()
