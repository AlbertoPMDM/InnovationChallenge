import sys
from PyQt5 import QtCore
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont

__version__ = "0.1"
__author__="UwU"

class MplCanvas(FigureCanvasQTAgg):
    """
    Makes a plot widget
    """
    def __init__(self, parent=None, width=1, height=1,dpi = 100):
        fig = Figure(figsize=(width,height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class buttonGrid(QGridLayout):
    """
    makeks a button widget but like with a grid {text: (x, y),...}
    """
    def __init__(self, buttons, funcs, width = 320, height = 150):
        super().__init__()

        #create and add buttons to layout
        for btnText, pos in buttons.items():
            buttons[btnText] = QPushButton(btnText)
            buttons[btnText].setFixedSize(width,height)
            buttons[btnText].clicked.connect(funcs[btnText]())
            super().addWidget(buttons[btnText], pos[0], pos[1])

class timer(QWidget):
    """
    CReate a global timer widget
    """
    def __init__(self):
        super().__init__()

        self.stopwatch = QLabel()
        self.stopwatch.setStyleSheet("border :3px solid black;")
        self.stopwatch.resize(320,300)
        self.stopwatch.setFont(QFont('Arial', 60))
        self.generalLayout = QVBoxLayout()
        self.setLayout(self.generalLayout)
        self.generalLayout.addWidget(self.stopwatch)

        self.startTime = time.time()
        self.endTime = time.time()
        def timeConvert():
            
            self.timeLapsed = self.endTime - self.startTime
            
            self.mins = self.timeLapsed // 60
            self.sec = self.timeLapsed % 60
            self.hours = self.mins // 60
            self.mins = self.mins % 60
            self.stopwatch.setText("{0}:{1}:{2}".format(int(self.hours),int(self.mins),int(self.sec)))

            self.endTime = time.time()

        self.updater = QtCore.QTimer()
        self.updater.timeout.connect(lambda:timeConvert())
        
class StartGui(QWidget):
    """
    Extra window/widget for 'start
    """
    def __init__(self):
        super().__init__()
        self.generalLayout = QVBoxLayout()
        self.label = QLabel("INICIAR")
        self.setLayout(self.generalLayout)

        self.generalLayout.addWidget(self.label)

        self.timer = timer()

        self.startButton = (0,0)
        self.startButton = QPushButton()
        self.startButton.setFixedSize(320,150)
        self.startButton.clicked.connect(lambda:self.timer.updater.start(1000))
        self.generalLayout.addWidget(self.timer)
        self.generalLayout.addWidget(self.startButton)

class MainGui(QMainWindow):
    """
    Program's GUI class
    """
    def __init__(self):
        """
        GUI initializer
        """ 
        super().__init__()
        #GUI properties
        self.setWindowTitle("application")
        self.setFixedSize(360,690)

        #Create central GUI and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        #create plot widget
        plt = MplCanvas(self, width=1, height=1, dpi=100)
        plt.axes.plot([0,1,2,3],[0,1,2,3])

        #create buttons
        self.startButtonSet = {
            "INICIAR":(0,0),
            "RUTINA":(1,0)
        }
        start = StartGui()
        routine = StartGui()
        self.startButtonFncs = {
            "INICIAR":lambda:start.show,
            "RUTINA":lambda:routine.show
        }
        interfaceButtons = buttonGrid(self.startButtonSet, self.startButtonFncs, 320, 150)
        downButton = buttonGrid({"down":(0,0)},{"down":lambda:start.show}, 320, 50)

        self.generalLayout.addWidget(plt)
        self.generalLayout.addLayout(interfaceButtons)
        self.generalLayout.addLayout(downButton)
    
def main():
    """
    Main function
    """
    #create an instance of the QApplication
    app = QApplication([])

    #Show the GUI
    view = MainGui()
    view.show()

    #execute the main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
