import pickle
import random
import os

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
from colors.bcolor import bcolors
from generating_models.core.data_preparation import fetchData

from ui.uimanager import clean


def prepareData(data: list[dict]):
    random.shuffle(data)
    test = data
    test_x = [(d["z"], d["n"]) for d in test]
    
    return test_x

def predicting(filename):
    with open(f"models/{filename}", "rb") as file:
        
        data = fetchData()
        test_x = prepareData(data)

        total = len(test_x)
        
        x_points = [[], []]
        y_points = [[], []]
        
        model = pickle.load(file)
        for i in range(0, total):
            test_sample_x = test_x[i]
            
            prediction = model.predict([test_sample_x])
            clean()
            print(f"{bcolors.OKGREEN}predicting the elements...")
            
            x_points[round(prediction[0][0])].append(test_sample_x[1])
            y_points[round(prediction[0][0])].append(test_sample_x[0])
            
            print(f"{bcolors.OKGREEN}progress: {round((len(y_points[0])/total) * 100)}%")
        clean()
        print("done!")
        return x_points, y_points
        


def start_model_prediction_visualisation(filename):
    App = QApplication(sys.argv)
    
    x_points, y_points = predicting(filename)
    colors = [[255, 0, 255], [255, 255, 255]]
    
    # create the instance of our Window
    window = Window(x_points, y_points, colors)
    
    # start the app
    sys.exit(App.exec())