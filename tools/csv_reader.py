import json

def read_json(file_name: str):
    with open(file_name) as file:
        data = json.load(file)
        entity = [
            {
                "symbol": data["elements"][int(data["nucs"][i]["z"])],
                "z": float(data["nucs"][i]["z"]),
                "n": float(data["nucs"][i]["n"]),
                "isStable": 1.0 if "h" in data["nucs"][i] and data["nucs"][i]["h"] == "stable" else 0.0,
                # "result": data["nucs"][i][],
            }
            for i in range(len(data["nucs"]))
        ]
        return entity