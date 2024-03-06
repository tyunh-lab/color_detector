import json

def setup_json(data_to_write = {"status": "seetupping", "now_task" : "ball_ditect"}):
    print(data_to_write)
    with open('data.json', 'w') as f:
        json.dump(data_to_write, f)

def read_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def write_json(data_to_write):
    with open('data.json', 'w') as f:
        json.dump(data_to_write, f)

#　上書き用
def write_json_overwrite(data_to_write):
    original_data = read_json()
    for key in data_to_write:
        original_data[key] = data_to_write[key]
    with open('data.json', 'w') as f:
        json.dump(original_data, f)