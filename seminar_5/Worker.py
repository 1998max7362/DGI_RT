from PyQt5.QtCore import QObject, pyqtSignal as Signal, pyqtSlot as Slot
from copy import deepcopy

class Worker(QObject):
    succes = Signal(object)
    error = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self.fnc = lambda *args: None
        self.result = None
    
    def setWork(self, fnc):
        self.fnc = fnc
    
    def getresult(self):
        return deepcopy(self.result)

    @Slot(object)
    def do_work(self):
        try:
            self.result = self.fnc()
            self.succes.emit(True)
        except:
            self.error.emit(True)
