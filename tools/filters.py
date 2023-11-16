def filter_by(arr: list[dict], key: str, value: str):
    return [d for d in arr if d[key] == value]
