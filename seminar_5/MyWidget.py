from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from seminar_4_bmstu.AudioItem import Audio_Item
from seminar_5.GraphWidgetV2 import GraphWidget
from math import ceil


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400)

        mainLayout = QHBoxLayout()
        verticalLayout = QVBoxLayout()

        mainLayout.addLayout(verticalLayout)
        
        self.setLayout(mainLayout)

        self.myLable=QLabel('Выбранный файл: ')
        self.graphWidget = GraphWidget()


        select_file_button = QPushButton('Выбрать файл')
        osc_button = QPushButton('Показать осциллограмму')
        spectre_button = QPushButton('Показать спектр')

        verticalLayout.addWidget(self.myLable)
        verticalLayout.addWidget(select_file_button)
        verticalLayout.addWidget(spectre_button)
        verticalLayout.addWidget(osc_button)

        mainLayout.addWidget(self.graphWidget)

        select_file_button.clicked.connect(self.select_file)
        osc_button.clicked.connect(self.show_osc)
        spectre_button.clicked.connect(self.show_spectr)

        self.clicks_counter = 0

        filename, filter = QFileDialog.getOpenFileName()
        self.audio_item = Audio_Item(filename)
        self.myLable.setText(f'Выбранный файл: {filename}')
        print(self.audio_item)
    
    def show_osc(self):
        xdata = self.audio_item.time_scale
        ydata = self.audio_item.osc_data
        self.graphWidget.setData(xdata, ydata)

    def show_spectr(self):
        xdata = self.audio_item.freqs_scale[0:ceil(self.audio_item.num_of_samples/2)]
        ydata = self.audio_item.spectre_data[0:ceil(self.audio_item.num_of_samples/2)]
        self.graphWidget.setData(xdata, ydata)



app=QApplication([])
mainWidget = MyWidget()
mainWidget.show()
app.exec()