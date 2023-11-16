import pickle
import random

from tools.csv_reader import read_csv


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


with open("model.pkl", "rb") as file:
    data = fetchData()
    train_x, train_y, test_x, test_y = prepareData(data)

    model = pickle.load(file)
    for i in range(0, 9):
        test_sample_x = test_x[i]
        test_sample_y = test_y[i]
        prediction = model.predict([test_sample_x])
        print(round(prediction[0][0]))
        print(test_sample_y)
