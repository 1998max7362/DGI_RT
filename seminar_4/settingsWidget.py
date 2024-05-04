import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import pyqtSignal


class SettingsWidget(QWidget):
    file_added = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        layout.addWidget(self._add_file_group_box())
        layout.addWidget(self._add_plot_froup_box())
        self._init_connections()

    def _add_file_group_box(self):
        file_group_box = QGroupBox()
        layout = QVBoxLayout()
        file_group_box.setLayout(layout)

        self.add_file_button = QPushButton("Выбрать файл")
        self.show_file_name_label = QLabel()

        layout.addWidget(self.add_file_button)
        layout.addWidget(self.show_file_name_label)

        return file_group_box

    def _add_plot_froup_box(self):
        plot_group_box = QGroupBox("График")
        layout = QVBoxLayout()
        plot_group_box.setLayout(layout)

        self.show_osc_button = QPushButton("Показать осцилограмму")
        self.show_spectre_button = QPushButton("Показать спектр")

        layout.addWidget(self.show_osc_button)
        layout.addWidget(self.show_spectre_button)

        return plot_group_box

    def _init_connections(self):
        self.add_file_button.clicked.connect(self._add_filename)

    def _add_filename(self):
        fileName, filter = QFileDialog.getOpenFileName()
        if fileName != '':
            self.file_name = fileName
            self.show_file_name_label.setText(fileName)
            self.file_added.emit(fileName)


if __name__ == '__main__':

    app = QApplication([])
    main = SettingsWidget()
    main.show()

    sys.exit(app.exec_())
