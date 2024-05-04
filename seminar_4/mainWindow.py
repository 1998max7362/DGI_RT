import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSize
from seminar_4.settingsWidget import SettingsWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное окно')
        self.setMinimumSize(QSize(1080,720)) # размер окна в пикселях

        self.settings_widget=SettingsWidget()

        self.setCentralWidget(self.settings_widget)

        self._init_connections()


    def _init_connections(self):
        self.settings_widget.file_added.connect(self.print_file_name)


    def print_file_name(self,filename):
        print("Выбранный файла:",filename)


if __name__ == '__main__':

    app = QApplication([])
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())