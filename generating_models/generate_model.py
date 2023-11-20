import json
import math
import pickle
import random

import keras
import numpy as np
from tqdm import tqdm

from tools.csv_reader import read_json
from tools.filters import filter_by
from colors.bcolor import bcolors
import os

def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')


    # For macOS and Linux
    else:
        _ = os.system('clear')


def map_half_life(half_life):
    if half_life != "STABLE":
        return 1 / float(half_life)
    else:
        return 1.0


def fetchData():
    data = read_json('./dataset/data.json')
    return data


def preprocessData(data: list[dict]):
    modified_data = []
    z_numbers = set([d["z"] for d in data])
    for z in z_numbers:
        elements = [d for d in data if d["z"] == z]
        stable_elements = [element for element in elements if element["isStable"] == 1.0]
        unstable_elements = [element for element in elements if element["isStable"] == 0.0]
        
        if len(unstable_elements) == 0.0:
            modified_data.extend(elements)
            continue
        
        if len(stable_elements) == 0:
            continue
            
        if len(stable_elements) / len(unstable_elements) < 0.05:
            for i in range(len(stable_elements)):
                modified_data.append(stable_elements[i])
                modified_data.append(unstable_elements[i])
            continue
        
        modified_data.extend(elements)
    return modified_data

def prepareData(data: list[dict]):
    data = preprocessData(data)
    random.shuffle(data)
    train = data[400:]
    test = data[:400]
    train_x = [(d["z"], d["n"]) for d in train]
    train_y = [(d["isStable"]) for d in train]
    test_x = [(d["z"], d["n"]) for d in test]
    test_y = [(d["isStable"]) for d in test]
    return train_x, train_y, test_x, test_y


def createModel():
    model = keras.Sequential(
        [
            keras.Input(shape=(2,), name="input"),
            keras.layers.Dense(
                120,
                activation=keras.activations.relu,
            ),
            keras.layers.Dense(
                5,
                activation=keras.activations.elu,
            ),
            keras.layers.Dense(
                1, activation=keras.activations.sigmoid, name="predictions"
            ),
        ]
    )
    # model.summary()
    model.compile(
        optimizer=keras.optimizers.Adam(0.001),  # Optimizer
        loss=keras.losses.binary_crossentropy,
        metrics=[keras.metrics.BinaryAccuracy()],
    )

    return model

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
