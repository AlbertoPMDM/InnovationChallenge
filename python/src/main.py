import sys
from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow

def main():
    """
    Main function
    """
    #create an instance of the QApplication
    app = QApplication([])

    #Show the GUI
    view = MainWindow()
    view.show()

    #execute the main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()