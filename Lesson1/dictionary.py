# Dictionary - CRUD

# Create - Khởi tạo
dict1 = {}
dict2 = {
    # Cặp giá trị key - value
    'name': 'Duc Trung',
    'age': 2,
    'address': 'Ha Noi' 
}

# Read - Duyệt, hiện phần tử
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
    print(f"{key}: {value}")
    # Truy cập bằng key
print('Tên:', dict2['name'])
    # Sử dụng phương thức get()
print('Tuổi:', dict2.get('age'))
        # Không tồn tại key => None / Giá trị mặc định
print('Money:', dict2.get('money', '404 not found'))

# Update - chỉnh sửa
    # Add cặp key - value
dict2['children'] = 'Hai meme'
    # Update giá trị
dict2['children'] = 'Khoa Nguyen'

# Delete - xóa phần tử
    # del - xóa phần tử theo key
del dict2['children']
    # pop - xóa phần tử theo key, trả về giá trị
dict2.pop('address')

# Kiểm tra key xem có tồn tại không
print('name' in dict2)      # True
print('money' in dict2)     # False

# Lấy tất cả key bằng phương thức keys()
print(dict2.keys())
# Lấy tất cả value bằng phương thức values()
print(dict2.values())
# Lấy tất cả key - value bằng phương thức items()
print(dict2.items())