from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
import time
from PyQt5.QtGui import QFont


class TimerModule(QWidget):
    """
    CReate a global timer widget
    """
    def __init__(self):
        """
        Constructor of timer
        """
        super().__init__()

        #Creates a Label that will be updated and used as stopwatch
        self.stopwatch = QtWidgets.QLabel()
        self.stopwatch.setStyleSheet("border :3px solid black;")
        self.stopwatch.resize(320,300)
        self.stopwatch.setFont(QFont('Arial', 60))

        #Creates a general Layout
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.generalLayout)
        self.generalLayout.addWidget(self.stopwatch)

        #starts systime variables
        self.startTime = time.time()
        self.endTime = time.time()
        def timeConvert():
            """
            Gets the time difference, converts it into HH:MM:SS, and updates the label
            """
            self.timeLapsed = self.endTime - self.startTime
            
            self.mins = self.timeLapsed // 60
            self.sec = self.timeLapsed % 60
            self.hours = self.mins // 60
            self.mins = self.mins % 60
            self.stopwatch.setText("{0}:{1}:{2}".format(int(self.hours),int(self.mins),int(self.sec)))

            self.endTime = time.time()

        #stars a QTimer and connects it to timeConvert()
        self.updater = QtCore.QTimer()
        self.updater.timeout.connect(lambda:timeConvert())