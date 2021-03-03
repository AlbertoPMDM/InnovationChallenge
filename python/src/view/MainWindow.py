import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from model.ButtonGrid import ButtonGrid

#Class Imports

class MainWindow(QMainWindow):
    """
    Program's GUI class
    """

    def __init__(self):
        """
        GUI initializer
        """ 

        def dpass(self):
            """
            This is just to test buttons
            """
            pass

        super().__init__()

        #GUI properties
        self.setWindowTitle("application")
        self.setFixedSize(320,568)

        #Create central GUI and general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        #button dictionaries
        self.buttonPos ={
            "Exercise":(0,0),
            "Sleep":(0,1),
            "Entertainment":(1,0),
            "Productivity":(1,1)
        }
        self.buttonFuncs = {
            "Exercise":lambda:dpass,
            "Sleep":lambda:dpass,
            "Entertainment":lambda:dpass,
            "Productivity":lambda:dpass
        }

        #button Constructor
        self.buttonWidget = ButtonGrid(self.buttonPos, self.buttonFuncs, 160, 284)
        self.generalLayout.addLayout(self.buttonWidget)