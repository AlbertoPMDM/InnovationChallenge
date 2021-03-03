
from PyQt5.QtWidgets import QGridLayout, QPushButton

class ButtonGrid(QGridLayout):
    """
    makeks a button widget but like with a grid {text: (x, y),...}
    """
    def __init__(self, buttons, funcs, width = 320, height = 150):
        super().__init__()

        #create and add buttons to layout, also connects them to a function
        for btnText, pos in buttons.items():
            
            buttons[btnText] = QPushButton(btnText)
            buttons[btnText].setFixedSize(width,height)
            buttons[btnText].clicked.connect(funcs[btnText]())
            super().addWidget(buttons[btnText], pos[0], pos[1])