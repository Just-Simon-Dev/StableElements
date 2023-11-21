from tools.csv_reader import read_json
import random

def fetchData():
    data = read_json("./dataset/data.json")
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