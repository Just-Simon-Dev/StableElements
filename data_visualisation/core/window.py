import random


from tools.csv_reader import read_json

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

class Window(QMainWindow):
 
    def __init__(self, x_points: list[list[int]], y_points: list[list[int]], colors: list[list[int]]):
        super().__init__()
 
        # setting title
        self.setWindowTitle("PyQtGraph")
 
        # setting geometry
        self.setGeometry(100, 100, 2400, 1200)
 
        # icon
        icon = QIcon("skin.png")
 
        # setting icon to the window
        self.setWindowIcon(icon)

        self.scatters_x = x_points
        self.scatters_y = y_points
        self.colors = colors
        
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

        data = read_json("./dataset/data.json")
        
        for i in range(len(self.scatters_x)):
            x_points = self.scatters_x[i]
            y_points = self.scatters_y[i]
            
            R, G, B = self.colors[i]
            
            scatter = pg.ScatterPlotItem(
                size=10, brush=pg.mkBrush(30, R, G, B))
            
            # setting data to the scatter plot
            scatter.setData(x_points, y_points)

            # add item to plot window
            # adding scatter plot item to the plot window
            plot.addItem(scatter)

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
