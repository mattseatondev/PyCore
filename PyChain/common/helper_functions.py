import json

def pr(data):
    if isinstance(data, list) or isinstance(data, dict):
        print(json.dumps(data, indent=2))
    else: 
        print(data)