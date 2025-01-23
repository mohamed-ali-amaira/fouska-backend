from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


def verif(text):
    return text.isnumeric() and int(text) > 99


def ondulant(text):
    n = int(text)
    for i in range(0, len(text) - 2, 2):
        if not (text[i] == text[i+2] and text[i] != text[i+1]):
            return False
    return True


def Play():
    text = fen.lineEdit.text()

    if (verif(text)):
        if (ondulant(text)):
            fen.label_3.setText(f"{text} est un nombre ondulant !")

        else:
            fen.label_3.setText(f"{text} n'est pas un nombre ondulant !")

    else:
        fen.label_3.setText("Veillez introduire un nombre >= 100")


app = QApplication([])

fen = loadUi("ondulant.ui")

fen.pushButton.clicked.connect(Play)

fen.show()

app.exec()
