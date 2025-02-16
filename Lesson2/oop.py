# Bài 1: Xây dựng class Rectangle gồm:
# 	- Thuộc tính: width, height
# 	- Phương thức:
# 		+ cvi(): tính chu vi HCN
# 		+ dtich(): tính diện tích HCN
class Rectangle:
    # Khởi tạo
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Phương thức tính chu vi
    def cvi(self):
        return (self.width + self.height) * 2
    
    # Phương thức tính diện tích
    def dtich(self):
        return self.width * self.height
    
hcn1 = Rectangle(4,5)
print('Chu vi HCN 1:', hcn1.cvi())
print('Diện tích HCN 1:', hcn1.dtich())

# Bài 2: Xây dựng class BankAccount gồm:
# 	- Thuộc tính: 
# 		+ acc_number (số tài khoản)
# 		+ balance (số dư)
# 	- Phương thức:
# 		+ deposit(): nạp tiền vào tài khoản
# 		+ withdraw(): rút tiền và cập nhật số dư
class BankAccount:
    # Khởi tại thuộc tính
    def __init__(self, acc_number, balance):
        # acc_number là số tài khoản ngân hàng
        self.acc_number = acc_number
        # balance là số dư tài khoản
        self.balance = balance

    # Phương thức deposit - nạp tiền 
    def deposit(self, amount):
        # amount - số tiền nạp vào tài khoản
        if amount > 0:
            self.balance += amount
            print('Nạp tiền thành công!')
            print(f'Số dư {self.acc_number}: ${self.balance}')
        else:
            print('Số tiền nạp không hợp lệ!')
    
    # Phương thức withdraw - rút tiền
    def withdraw(self, amount):
        # amount - số tiền rút ra khỏi tài khoản
        if 0 < amount <= self.balance:
            self.balance -= amount
            print('Rút tiền thành công!')
            print(f'Số dư {self.acc_number}: ${self.balance}')
        else:
            print('Số tiền rút không hợp lệ!')

    def withdraw2(self):
        # amount - số tiền rút ra khỏi tài khoản
        amount = float(input('Nhập số tiền rút: '))

        # Kiểm tra số tiền rút
        while amount <= 0 or amount > self.balance:
            print(f'Số dư: {self.balance}')
            print('Số tiền rút không hợp lệ!')
            amount = float(input('Nhập số tiền rút: '))

        # Rút tiền
        self.balance -= amount
        print('Rút tiền thành công!')
        print(f'Số dư {self.acc_number}: ${self.balance}')

acc1 = BankAccount('Huy', 1)
print(f'\nSố dư ban đầu: ${acc1.balance}')
    # Nạp tiền
acc1.deposit(50)
    # Rút tiền
acc1.withdraw(30)
acc1.withdraw2()