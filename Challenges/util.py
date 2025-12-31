import json
import os

def pr(data):
    if isinstance(data, list) or isinstance(data, dict):
        print(json.dumps(data, indent=2))
    else:
        print(data)
        
def resolve_path(current_file:str, relative_path:str) -> str:
    base_dir = os.path.dirname(os.path.abspath(current_file))
    return os.path.abspath(os.path.join(base_dir, relative_path))

# def test:
#     print("HIT UTIL.py")