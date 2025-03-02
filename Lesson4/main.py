import oop

# Test data dạng dict (file json)
dtb = oop.PlayerDatabase()
print(len(dtb.players_dict))

# Test load data dạng object
dtb.load_data()
print(len(dtb.players_list))

# dtb.show_all()
print(dtb.find_player_by_name('Lionel Messi'))

# Lấy thuộc tính của đối tượng vừa tìm
find1 = dtb.find_player_by_name('Lionel Messi')
print(find1.club)

# Thêm 1 data mới
new_player = {
        "id": 10,
        "name": "Khai Hung",
        "dob": "16/10/2011",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 1
}
dtb.add_player(new_player)

# Sửa thông tin
edit_player = {
        "id": 10,
        "name": "Khai Hung",
        "dob": "16/10/2011",
        "region": "Vietnam",
        "club": "Roblox",
        "rating": 1.0,
        "worth": 2
}
dtb.edit_player('Khai Hung', edit_player)

# Xóa thông tin
dtb.delete_player('Khai Hung')