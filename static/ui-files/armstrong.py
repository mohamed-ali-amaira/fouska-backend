from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


def verif(text):
    return text.isnumeric() and len(text) < 5


def armstrong(text):
    s = 0
    for i in range(len(text)):
        s = s + int(text[i]) ** len(text)
    return s == int(text)


def Play():
    text = fen.lineEdit.text()
    if (verif(text)):
        if (armstrong(text)):
            fen.label_resultat.setText("Ce nombre est armstrong")
        else:
            fen.label_resultat.setText("Ce nombre n'est pas armstrong")
    else:
        fen.label_resultat.setText("Veillez entrer un X valide")


app = QApplication([])
fen = uic.loadUi("armstrong.ui")

fen.pushButton.clicked.connect(Play)

fen.show()
app.exec()
