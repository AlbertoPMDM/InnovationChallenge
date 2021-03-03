from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from model.TimerModule import TimerModule

class ExerciseStart(QWidget):
    """
    Extra window/widget for 'start
    """
    def __init__(self):
        """
        Constructor of the Start button GUI
        """

        super().__init__()
        
        #CReate general Layout for class
        self.generalLayout = QVBoxLayout()
        self.setLayout(self.generalLayout)

        #CReates a timer class stopwatch, if that makes sense
        self.timer = TimerModule()

        #CReates the start stopwatch button
        self.startButton = (0,0)
        self.startButton = QPushButton("START")
        self.startButton.setFixedSize(320,150)
        self.startButton.clicked.connect(lambda:self.timer.updater.start(1000))
        self.generalLayout.addWidget(self.timer)
        self.generalLayout.addWidget(self.startButton)

        #create
        self.stopButton = (0,1)
        self.stopButton = QPushButton("STOP")
        self.stopButton.setFixedSize(320,150)
        self.stopButton.clicked.connect(lambda:self.timer.updater.stop())
        self.generalLayout.addWidget(self.stopButton)