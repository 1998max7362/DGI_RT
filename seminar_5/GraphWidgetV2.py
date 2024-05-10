import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # a figure instance to plot on
        self.figure = plt.figure()
  
        # this is the Canvas Widget that 
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
  
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
    
    def setData(self, xdata,ydata):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(xdata,ydata)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication([])
    main = GraphWidget()
    main.show()
    sys.exit(app.exec_())