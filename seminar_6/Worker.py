from PyQt5.QtWidgets import QWidget, QGroupBox, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QTextEdit
from PyQt5.QtCore import QObject, QThread, pyqtSignal as Signal, pyqtSlot as Slot
from copy import deepcopy


class Worker(QObject):
    finished = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self.fnc = lambda: None
        self.interrupted = False

    def setWork(self, fnc):
        self.fnc = fnc

    @Slot(object)
    def runWork(self):
        try:
            self.result = self.fnc()
            message = {'status': 'success', 'result': self.result}
            self.finished.emit(message)
        except Exception as e:
            message = {'status': 'error', 'result': e}
            self.finished.emit(message)


class TaskExecuter(QThread):
    taskStartRequested = Signal(object)
    taskFinished = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self.worker = Worker()
        self.worker.moveToThread(self)
        self.start()

        self.__taskResult = None
        self.__taskIsRunning = False
        self.worker.finished.connect(self.__setTaskResult)

        self.taskStartRequested.connect(self.worker.runWork)

    def setTask(self, task):
        self.worker.setWork(task)

    def runTask(self):
        if not self.__taskIsRunning:
            self.taskStartRequested.emit(True)
            self.__taskIsRunning = True
        else:
            print('Уже запущено')

    def stopTask(self):
        self.__restartThread()
        message = {'status': 'interrupted', 'result': None}
        self.__setTaskResult(message)

    def getTaskResult(self):
        return deepcopy(self.__taskResult)

    def __setTaskResult(self, result):
        self.__taskResult = result
        self.taskFinished.emit(deepcopy(self.__taskResult))
        self.__taskIsRunning = False
        print(self.__taskResult)

    def __restartThread(self):
        self.terminate()
        self.worker = Worker()
        self.worker.moveToThread(self)
        self.start()
