import pickle
import random
from colors.bcolor import bcolors
from generating_models.core.data_preparation import fetchData
from testing_models.core.data_preparation import prepareData

from ui import uimanager


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
            uimanager.clean()
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
