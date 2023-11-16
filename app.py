import json
import math
import pickle
import random

import keras
import numpy as np
from tqdm import tqdm

from tools.csv_reader import read_csv
from tools.filters import filter_by


def map_half_life(half_life):
    if half_life != "STABLE":
        return 1 / float(half_life)
    else:
        return 1.0


def fetchData():
    data = read_csv("livechart.csv")
    val_data = [d for d in data if not d["half_life_sec"] == ""]
    needed_data = [
        {
            "symbol": d["symbol"],
            "z": float(d["z"]),
            "n": float(d["n"]),
            "half_life": map_half_life(d["half_life_sec"]),
            "SF": 1.0 if "A" in (d["decay_1"], d["decay_2"], d["decay_3"]) else 0.0,
        }
        for d in val_data
    ]

    return needed_data


def prepareData(data: list[dict]):
    random.shuffle(data)
    train = data[600:]
    test = data[:600]
    train_x = [(d["z"], d["n"], d["half_life"]) for d in train]
    train_y = [(d["SF"]) for d in train]
    test_x = [(d["z"], d["n"], d["half_life"]) for d in test]
    test_y = [(d["SF"]) for d in test]
    return train_x, train_y, test_x, test_y


def createModel():
    model = keras.Sequential(
        [
            keras.Input(shape=(3,), name="input"),
            keras.layers.Dense(
                9,
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


best_model = None

for i in tqdm(range(0, 10)):
    data = fetchData()

    train_x, train_y, test_x, test_y = prepareData(data)

    model = createModel()
    model.fit(
        np.array(train_x),
        np.array(train_y),
        epochs=30,
        validation_data=(np.array(test_x), np.array(test_y)),
        verbose=False,
    )

    # print(model.get_metrics_result())
    # print(np.array(test_x[0]).shape)

    predict_x = np.array([test_x[0]])
    predict_y = model.predict(predict_x)

    if math.isnan(predict_y[0][0]):
        continue
    # print(test_y[0])

    if best_model is None:
        best_model = model
    print()
    if (
        best_model.get_metrics_result()["binary_accuracy"]
        < model.get_metrics_result()["binary_accuracy"]
    ):
        best_model = model

print(best_model)
model_pkl_file = "model2.pkl"
print(best_model.get_metrics_result())
with open(model_pkl_file, "wb") as file:
    pickle.dump(best_model, file)
