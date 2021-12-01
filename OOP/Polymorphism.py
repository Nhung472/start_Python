#Tính đa hình
#nhiều lớp sẽ có chung phương thức nhưng được thực hiện 1 hành động theo nhiều cách khác nhau

class Toyota:
    def dungxe(self):
        print("Toyota dừng xe để nạp điện")
    def nomay(self):
        print("Toyota nổ máy bằng hộp số tự động")

class Porsche:
    def dungxe(self):
        print("Porsche dừng xe để bơm xăng")
    def nomay(self):
        print("Porsche nổ máy bằng hộp số cơ")
# common interface
def kiemtra_dungxe(car): car.dungxe()

toyota = Toyota()
porsche = Porsche()

kiemtra_dungxe(toyota)
kiemtra_dungxe(porsche)