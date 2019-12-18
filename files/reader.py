import json


def file_open(path, filename):
    with open(path + filename) as f:
        data = json.load(f)
    return data
