from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi


def verif(text):
    return text.isnumeric() and int(text) > 0


def superpair(text):
    n = int(text)
    if (n % 2 != 0):
        return False
    for i in range(len(text)):
        if (int(text[i]) % 2 != 0):
            return False
    for i in range(2, ((n // 2) + 1)):
        if (n % i == 0 and i % 2 != 0):
            return False
    return True


def Play():
    text = fen.lineEdit.text()

    if (verif(text)):
        if (superpair(text)):
            fen.label_3.setText(f"{text} est un super pair plus !")

        else:
            fen.label_3.setText(f"{text} n'est pas un super pair plus !")

    else:
        fen.label_3.setText("Veillez introduire un nombre > 0")


app = QApplication([])

fen = loadUi("superpairplus.ui")

fen.pushButton.clicked.connect(Play)

fen.show()

app.exec()
