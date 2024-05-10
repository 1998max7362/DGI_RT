import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
import pyqtgraph as pg
import numpy as np


class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        # self.x = np.array([1, 2, 3])
        # self.y = np.array([3, 2, 1])

        self.plotWidget = pg.PlotWidget()
        layout.addWidget(self.plotWidget)

    def setData(self, xdata, ydata):
        self.plotWidget.plot(xdata, ydata)


if __name__ == '__main__':
    app = QApplication([])
    main = GraphWidget()
    main.show()
    sys.exit(app.exec_())
