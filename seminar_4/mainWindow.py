import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное окно')
        self.setMinimumSize(QSize(1080,720)) # размер окна в пикселях

        self.setCentralWidget()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())