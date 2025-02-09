# Lập trình hướng đối tượng
# OOP - Object oriented programming

# Tổng quát: OOP là cách chúng ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Attribute (thuộc tính): Đặc điểm của đối tượng
# Method (phương thức): Hành động của đối tượng

# Ví dụ: class Human (con người)
    # Thuộc tính (đặc điểm): tên, tuổi, giới tính,..
    # Phương thức (hành động): ăn, ngủ, nói chuyện, hát,..

# Khai báo lớp đối tượng
class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (hành động)
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi.')

    # Phương thức hát
    def sing(self, song):
        print(f'{self.name} đang hát: {song}')