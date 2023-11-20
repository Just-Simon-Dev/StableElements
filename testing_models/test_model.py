import pickle
import random
from colors.bcolor import bcolors
import os

from tools.csv_reader import read_json

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
    data = read_json("./dataset/data.json")
    return data


def prepareData(data: list[dict]):
    random.shuffle(data)
    test = data
    test_x = [(d["z"], d["n"]) for d in test]
    test_y = [(d["isStable"]) for d in test]
    return test_x, test_y

def start_testing(filename:str):
    with open(f"models/{filename}", "rb") as file:
        
        data = fetchData()
        test_x, test_y = prepareData(data)

        success = 0
        failed = 0
        total = len(test_y)
        
        model = pickle.load(file)
        for i in range(0, total):
            test_sample_x = test_x[i]
            test_sample_y = test_y[i]
            prediction = model.predict([test_sample_x])
            clean()
            print(f"{bcolors.OKGREEN}testing...")
            if round(prediction[0][0]) == test_sample_y:
                success+=1
            else:
                failed += 1
            print(f"{bcolors.OKGREEN}progress: {round(((success + failed)/total) * 100)}%")
        
        print(f"sucess = {success}")
        print(f"failed = {failed}")
        print(f"total = {total}")
        print(f"accuracy = {round((success / total) * 100)}%")
