from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QTextEdit
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from seminar_6.Worker import TaskExecuter
import time


class ChatWindow(QWidget):
    work_requested = Signal(object)

    def __init__(self):
        super().__init__()

        # Устанавливаем минимальные размеры окна
        self.setMinimumSize(600, 400)

        # Создаем и устанавливаем горизонтальный макет на всё окно
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        self.label = QLabel('Счетчик: ')
        startButton = QPushButton('Старт', clicked=self.startClicked)
        stopButton = QPushButton('Стоп', clicked=self.stopClicked)


        mainLayout.addWidget(self.label)
        mainLayout.addWidget(startButton)
        mainLayout.addWidget(stopButton)

        # self.taskInProgress = False
        self.taskExecuter = TaskExecuter()
    
    def startClicked(self):
        # self.taskInProgress = True
        self.taskExecuter.setTask(lambda: self.__fakeTask())
        self.taskExecuter.runTask()

    def stopClicked(self):
        self.taskExecuter.stopTask()

    def __fakeTask(self):
        counter = 0
        while True:
            self.label.setText(f'Счетчик: {counter}')
            time.sleep(1)
            counter += 1


if __name__ == '__main__':
    app = QApplication([])
    mainWidget = ChatWindow()
    mainWidget.show()
    app.exec()
