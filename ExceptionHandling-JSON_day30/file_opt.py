from datetime import datetime
from os import linesep
import json

def write(data_dict):
    try: 
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(data_dict)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(data_dict, file, indent=4)
    else:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
            
            
def Search(web_name):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if web_name in data:
                return data[web_name]
            else:
                return -1
    except FileNotFoundError:
        return -1
    