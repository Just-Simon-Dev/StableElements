import csv


def read_csv(file_name: str):
    with open(file_name, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        data = [s for s in spamreader]
        dict_data = [
            {data[0][j]: v for j, v in enumerate(d)}
            for i, d in enumerate(data)
            if i > 0 and d != []
        ]
        return dict_data
