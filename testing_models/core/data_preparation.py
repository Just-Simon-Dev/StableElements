import random

def prepareData(data: list[dict]):
    random.shuffle(data)
    test = data
    test_x = [(d["z"], d["n"]) for d in test]
    test_y = [(d["isStable"]) for d in test]
    return test_x, test_y