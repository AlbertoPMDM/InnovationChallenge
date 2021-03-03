import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvasModule(FigureCanvasQTAgg):
    """
    Makes a plot widget
    """
    def __init__(self, parent=None, width=1, height=1,dpi = 100):
        #Creates a 111 plot with one 'graph', it normally auto-adjusts to the size of the window, and resizing doesnt seem to work as in matplotlib
        fig = Figure(figsize=(width,height), dpi = dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvasModule, self).__init__(fig)