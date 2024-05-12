from PyQt5.QtWidgets import QWidget, QGroupBox, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal as Signal, pyqtSlot as Slot
from seminar_5.AudioItem import Audio_Item
from seminar_5.GraphWidgetV2 import GraphWidget
from datetime import datetime
from math import ceil
from seminar_5.Worker import Worker


def getDateTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class MyWidget(QWidget):
    work_requested = Signal(object)
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 400)

        mainLayout = QHBoxLayout()

        leftWidget = QWidget()
        verticalLayout = QVBoxLayout()
        leftWidget.setLayout(verticalLayout)
        leftWidget.setMaximumWidth(400)

        mainLayout.addWidget(leftWidget)

        self.setLayout(mainLayout)

        self.myLable = QLabel('Лог:')
        self.myTextEdit = QTextEdit()
        self.myTextEdit.setReadOnly(True)
        self.graphWidget = GraphWidget()

        select_file_button = QPushButton('Выбрать файл')
        osc_button = QPushButton('Показать осциллограмму')
        spectre_button = QPushButton('Показать спектр')

        verticalLayout.addWidget(self.myLable)
        verticalLayout.addWidget(self.myTextEdit)
        verticalLayout.addWidget(select_file_button)
        verticalLayout.addWidget(spectre_button)
        verticalLayout.addWidget(osc_button)

        mainLayout.addWidget(self.graphWidget)

        select_file_button.clicked.connect(self.select_file)
        osc_button.clicked.connect(self.show_osc)
        spectre_button.clicked.connect(self.show_spectr)

        self.audio_item = False

        self.worker_thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)
        self.work_requested.connect(self.worker.do_work)
        self.worker_thread.start()
    
    def start_work(self):
        self.work_requested.emit(True)

    def select_file(self):
        filename, _ = QFileDialog.getOpenFileName()
        if filename:
            self.addLog(f'Выбран файл: {filename}')
            self.worker.setWork(lambda: self.__loadFile(filename))
            self.start_work()
    
    def __loadFile(self, filename):
        try:
            self.audio_item =  Audio_Item(filename)
        except:
            self.audio_item = False
            self.addLog("Ошибка чтения файла")
        


    def show_osc(self):
        self.worker.setWork(self.__buldOsc)
        if self.audio_item:
            self.addLog('Расчет осциллограммы...')
            self.start_work()
        else:
            self.addLog('Не выбран файл')

    def __buldOsc(self):
        xdata = self.audio_item.time_scale
        ydata = self.audio_item.osc_data
        self.graphWidget.setData(xdata, ydata)
        self.addLog('Успешно')

    def show_spectr(self):
        self.worker.setWork(self.__buldSpectre)
        if self.audio_item:
            self.addLog('Расчет осциллограммы...')
            self.start_work()
        else:
            self.addLog('Не выбран файл')
    
    def __buldSpectre(self):
        xdata = self.audio_item.freqs_scale[0:ceil(
            self.audio_item.num_of_samples/2)]
        ydata = self.audio_item.spectre_data[0:ceil(
            self.audio_item.num_of_samples/2)]
        self.graphWidget.setData(xdata, ydata)
        self.addLog('Успешно')

    def addLog(self, text):
        self.myTextEdit.insertPlainText(
            f'{getDateTime()} >> {text} \n')


app = QApplication([])
mainWidget = MyWidget()
mainWidget.show()
app.exec()
