# Press the green button in the gutter to run the script.
from PyQt5.QtWidgets import QApplication
from ui import Ui

if __name__ == '__main__':
    app = QApplication([])
    window = Ui()
    app.exec_()
