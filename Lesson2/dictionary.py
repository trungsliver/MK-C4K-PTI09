# Hàm map(function, itertable)
    # function: hàm biến đổi phần tử
    # itertable: đối tượng dữ liệu

# Ví dụ: Cho cho danh sách điểm hệ số 10
# Yêu cầu: dùng map() để chuyển đổi danh sách sang hệ số 4
gpa_10 = [5, 7, 8, 10, 9]
    # Cách 1: lambda - hàm không xác định / hàm ẩn danh
gpa_4 = map(lambda gpa: gpa/10 * 4, gpa_10)
# gpa_44 = []
# for gpa in gpa_10:
#     new_gpa = gpa / 10 * 4
#     gpa_44.append(new_gpa)
print(list(gpa_4))
    # Cách 2: Dùng hàm xác định
def convert_gpa(score):
    return score / 10 * 4
gpa_4 = map(convert_gpa, gpa_10)
print(list(gpa_4))

# DICTIONARY & MAP
# Bài 1: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
# Ví dụ: tRunG -> TRUNG
pti09 = ['kHaI hUng', 'miNH tAm', 'mInH dUC', 'kHoA nGuYEn']
    # Cách 1: lambda - hàm không xác định / hàm ẩn danh 
pti09_1 = map(lambda stu: str.upper(stu), pti09)
print(list(pti09_1))
    # Cách 2: Dùng hàm xác định
def convert_to_upper(item):
    return str.upper(item)
pti09_2 = map(convert_to_upper, pti09)
print(list(pti09_2))

# Bài 2: Quản lý thông tin sinh viên
# #Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    "name": "John",
    "age": 22,
    "grade": "A"
}
# 2. Cập nhật grade của sinh viên thành "A+".
student["grade"] = "A+"
# 3. Xóa thông tin age của sinh viên.
del student["age"]
# 4. Kiểm tra xem name có trong dictionary không.
print('name' in student)

# Bài 3: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'
def word_count(sentence):
    words = sentence.strip().split()
    # mỗi từ là 1 key, số lần xuất hiện là value
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict
print(word_count(sentence))

# Bài 4: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}
def merge_dict(dict1, dict2):
    # copy dict1 để đảm bảo dữ liệu không bị thay đổi
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        # Nếu key đã tồn tại trong dict1, cộng giá trị
        # Nếu key chưa tồn tại, để giá trị mặc định = value(dict2)
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict
print(merge_dict(A, B))

# Bài 5: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
grade = {
    'Khải Hưng': 2,
    'Minh Tâm': 7,
    'Minh Đức': 6,
    'Khoa Nguyên': 5,
    'Hải meme': 10,
    'Bảo Nam': 4
}
def find_max_key(dictionary:dict):
    # sử dụng max() với key để tìm key có giá trị lớn nhất
    return max(dictionary, key=dictionary.get)
print(find_max_key(grade))

# Bài 6: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
grade = {
    'Khải Hưng': 2,
    'Minh Tâm': 7,
    'Minh Đức': 6,
    'Khoa Nguyên': 5,
    'Hải meme': 10,
    'Bảo Nam': 4
}
def sort_dict_by_value(my_dict):
    # sử dụng sorted() với key để sắp xếp dictionary
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sort_dict_by_value(grade))

# Bài 7: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'bomb': 3,
    'elderberry': 3
}
def group_by_value(my_dict):
    grouped_dict = {}
    for key, value in my_dict.items():
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict
print('\n',group_by_value(data))

# Bài 8: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))
