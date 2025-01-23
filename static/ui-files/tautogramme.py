from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def verif(text):
    for i in range(len(text)):
        if (text[i] != " " and text[i] not in ABC):
            return False

    return len(text) < 160 and len(text) != 0


def tautogramme(text):
    l = text[0]
    for i in range(len(text)):
        if (text[i] == " " and i < len(text) - 1):
            if (text[i + 1] != l):
                return False
    return True


def Play():
    text = fen.lineEdit.text()
    if (verif(text)):
        if (tautogramme(text)):
            fen.label_5.setText("c'est une chaine tautogramme ")
        else:
            fen.label_5.setText("ce n'est pas une chaine tautogramme ")
    else:
        fen.label_5.setText("ce n'est pas une chaine valide")


def annuler():
    fen.lineEdit.clear()


def quitter():
    fen.close()


app = QApplication([])

fen = loadUi("tautogramme.ui")


fen.pushButton.clicked.connect(Play)
fen.pushButton_2.clicked.connect(annuler)
fen.pushButton_3.clicked.connect(quitter)


fen.show()

app.exec()
