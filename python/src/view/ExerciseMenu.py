from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from model.ButtonGrid import ButtonGrid
from model.MplCanvasModule import MplCanvasModule
from view.ExerciseStart import ExerciseStart


class ExerciseMenu(QWidget):
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
        self.setLayout(self.generalLayout)

        #create plot widget
        plt = MplCanvasModule(self, width=1, height=1, dpi=100)
        plt.axes.plot([0,1,2,3],[0,1,2,3])

        #create buttons
        #Positions
        self.startButtonSet = {
            "INICIAR":(0,0),
            "RUTINA":(1,0)
        }
        #Creates two startGui() elements, because buttonGrid class requires functions to be passed, and there are no other buttons for now
        start = ExerciseStart()
        routine = ExerciseStart()
        #Functions
        self.startButtonFncs = {
            "INICIAR":lambda:start.show,
            "RUTINA":lambda:routine.show
        }

        #Creates the instances of the buttons
        interfaceButtons = ButtonGrid(self.startButtonSet, self.startButtonFncs, 320, 150)
        downButton = ButtonGrid({"down":(0,0)},{"down":lambda:start.show}, 320, 50)

        self.generalLayout.addWidget(plt)
        self.generalLayout.addLayout(interfaceButtons)
        self.generalLayout.addLayout(downButton)