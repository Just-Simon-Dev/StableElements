import pickle


def start():
    z = float(input("podaj z: "))
    n = float(input("podaj n: "))
    h = float(input("podaj połowiczny czas rozpadu: "))

    test_x = (z, n, 1 / h)

    labels = ["nie emituje cząstek alfa", "emituje cząstki alfa"]

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
        prediction = model.predict([test_x])
        index = round(prediction[0][0])
        print(labels[index])


if __name__ == "__main__":
    while True:
        start()

        a = input("Kolejna? (T/N)")
        if a not in ("T", "t", "\n", ""):
            break
