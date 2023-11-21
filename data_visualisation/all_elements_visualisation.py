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

from data_visualisation.core.window import Window
from generating_models.core.data_preparation import fetchData



def prepareData(data: list[dict]):
    random.shuffle(data)
    test = data
    
    x_points = [[d["n"] for d in test if d["isStable"] == 1.0], [d["n"] for d in test if d["isStable"] == 0.0]]
    y_points = [[d["z"] for d in test if d["isStable"] == 1.0], [d["z"] for d in test if d["isStable"] == 0.0]]
    
    return x_points, y_points

def start_all_elements_visualisation():
    App = QApplication(sys.argv)
    
    data = fetchData()
    x_points, y_points = prepareData(data)
    colors = [[255, 0, 255], [255, 255, 255]]
    
    # create the instance of our Window
    window = Window(x_points, y_points, colors)
    
    # start the app
    sys.exit(App.exec())