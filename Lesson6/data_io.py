import os, json

# Đọc dữ liệu (Read)
def load_json_data():
    user_dict_data = list()
    with open('users.json', 'r') as file:
        data = json.load(file)
    user_dict_data.extend(data)
    return user_dict_data

# Ghi dữ liệu (Write)
def write_json_data(json_data):
    with open('users.json', 'w') as file:
        json.dump(json_data, file)