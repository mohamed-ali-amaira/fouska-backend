from PyQt5.QtWidgets import QApplication

from PyQt5.uic import loadUi


ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

XYZ = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'


def verifier(text):
    if (len(text) > 30):
        return False
    for i in range(len(text)):
        if not text[i] in ABC:
            return False
    return True


def crypter(text):
    r = ""
    for i in range(len(text)):
        r += XYZ[ABC.find(text[i])]
    return r


def Play():
    text = fen.lineEdit.text()
    if (verifier(text)):
        t = crypter(text)
        fen.label_3.setText(t)

    else:
        fen.label_3.setText("Entrer un texte valide")
        fen.lineEdit.clear()


app = QApplication([])

fen = loadUi("cryptage.ui")

fen.pushButton.clicked.connect(Play)

fen.show()

app.exec()
