import json

def print_json():
    data = None
    with open("venues.json") as f:
        data = json.load(f)


    print(json.dumps(data, indent=4, sort_keys=True))

if __name__ == "__main__":
    print_json()