import json
import math
import pickle
import random

import keras
import numpy as np
from tqdm import tqdm

from tools.csv_reader import read_json
from tools.filters import filter_by

# importing Qt widgets
from PyQt5.QtWidgets import *
 
# importing system
import sys
 
# importing numpy as np
import numpy as np
 
# importing pyqtgraph as pg
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import json

def prepareData(data: list[dict]):
    random.shuffle(data)
    train = data[600:]
    test = data[:600]
    train_x = [(d["z"], d["n"]) for d in train]
    train_y = [(d["SF"]) for d in train]
    test_x = [(d["z"], d["n"]) for d in test]
    test_y = [(d["SF"]) for d in test]
    return train_x, train_y, test_x, test_y

class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("PyQtGraph")
 
        # setting geometry
        self.setGeometry(100, 100, 600, 500)
 
        # icon
        icon = QIcon("skin.png")
 
        # setting icon to the window
        self.setWindowIcon(icon)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
        
    def UiComponents(self):
    
        # creating a widget object
        widget = QWidget()

        # creating a plot window
        plot = pg.plot()

        # number of points
        n = 300

        # creating a scatter plot item
        # of size = 10
        # using brush to enlarge the of green color
        scatter = pg.ScatterPlotItem(
            size=10, brush=pg.mkBrush(30, 255, 255, 255))
        
        scatter_of_stable_elements = pg.ScatterPlotItem(
            size=10, brush=pg.mkBrush(30, 255, 0, 255))

        data = read_json("./dataset/data.json")
        x_points = [d["n"] for d in data if d["isStable"] == 0.0]
        y_points = [d["z"] for d in data if d["isStable"] == 0.0]
        
        x_stable_points = [d["n"] for d in data if d["isStable"] == 1.0]
        y_stable_points = [d["z"] for d in data if d["isStable"] == 1.0]

        # setting data to the scatter plot
        scatter.setData(x_points, y_points)
        
        scatter_of_stable_elements.setData(x_stable_points, y_stable_points)

        # add item to plot window
        # adding scatter plot item to the plot window
        plot.addItem(scatter)
        plot.addItem(scatter_of_stable_elements)

        # Creating a grid layout
        layout = QGridLayout()


        # setting this layout to the widget
        widget.setLayout(layout)

        # plot window goes on right side, spanning 3 rows
        layout.addWidget(plot, 0, 1, 3, 1)

        # setting this widget as central widget of the main window
        self.setCentralWidget(widget)

        # setting points
        scatter.addPoints(x_points, y_points)

def start():
    App = QApplication(sys.argv)
 
    # create the instance of our Window
    window = Window()
    
    # start the app
    sys.exit(App.exec())