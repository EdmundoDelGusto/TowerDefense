import json
class Loader:
    def __init__(self, path_to_json):
        with open(path_to_json, 'r') as f:
            self.__dict__ = json.load(f)
