import json
import math
import pickle

import numpy as np
from tqdm import tqdm

from colors.bcolor import bcolors
from generating_models.core.data_preparation import fetchData, prepareData
from generating_models.core.model_generation import createModel

from ui.uimanager import clean

import os

def generate_model(iterations: int):
    best_model = None

    for i in tqdm(range(0, iterations)):
        data = fetchData()

        train_x, train_y, test_x, test_y = prepareData(data)

        model = createModel()
        model.fit(
            np.array(train_x),
            np.array(train_y),
            epochs=100,
            validation_data=(np.array(test_x), np.array(test_y)),
            verbose=False,
        )

        predict_x = np.array([test_x[0]])
        predict_y = model.predict(predict_x)

        if math.isnan(predict_y[0][0]):
            continue

        if best_model is None:
            best_model = model
        
        if (
            best_model.get_metrics_result()["binary_accuracy"]
            < model.get_metrics_result()["binary_accuracy"]
        ):
            best_model = model
            
        clean()
    
    print(f"{bcolors.OKBLUE}Our new model have accuracy: {bcolors.OKGREEN}{best_model.get_metrics_result()['binary_accuracy']}%")
    
    model_name = input(f"{bcolors.OKBLUE}Please type the name of the file: {bcolors.OKGREEN}")

    model_pkl_file = f"models/{model_name}.pkl"
    with open(model_pkl_file, "wb") as file:
        pickle.dump(best_model, file)
