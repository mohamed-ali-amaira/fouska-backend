from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


def verif(text):
    return text.isnumeric() and int(text) > 2 and int(text) < 100


def Play():
    text = fen.lineEdit.text()
    if (verif(text)):
        s = 0
        for i in range(len(text)):
            s = s + int(text[i])

        if int(text) % s == 0:
            fen.label_5.setText("c'est un nombre harshad")

        else:
            fen.label_5.setText("ce n'est pas un nombre harshad")

    else:
        fen.label_5.setText("Entrer un entier valide")
        fen.lineEdit.clear()


def annuler():
    fen.lineEdit.clear()


def quitter():
    fen.close()


app = QApplication([])

fen = loadUi("harshad.ui")

fen.pushButton.clicked.connect(Play)
fen.pushButton_2.clicked.connect(annuler)
fen.pushButton_3.clicked.connect(quitter)


fen.show()

app.exec()
