import os, json
import data_io

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # chỉ khi nào có thuộc tính thì mới update
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f"User: {self.username} \nPass: {self.password}")

class UserDatabase:
    def __init__(self):
        # Tạo danh sách chứa các player - dạng object
        self.users_list = list()
        # Đọc dữ liệu khi khởi tạo - dạng dict
        self.users_dict = data_io.load_json_data()

    # Chuyển đổi dữ liệu json sang object
    def load_data(self):
        new_users = []
        for user_data in self.users_dict:
            user = User(username = user_data["username"],
                        password = user_data["password"])
            new_users.append(user)
        self.users_list = new_users