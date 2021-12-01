#Tính kế thừa 
#thừa hưởng lại những thuộc tính, method từ 1 lớp khác, sử dụng hoặc override chúng

class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name 
        self.color = color
    def chayxe(self):
        print ("{} đang chạy trên đường".format(self.name))
    def use(self, purpose):
        print ("{} đang dừng xe để {}".format(self.name, purpose))
class Toyota(Car):
    def __init__(self, brand, name, color, material):
        # Gọi tới constructor của lớp cha (Car) để gán giá trị vào thuộc tính của lớp cha.
        super().__init__(brand, name, color)
        self.material = material
    def chayxe(self):
        print ("{} đang chạy trên đường".format(self.name))
    def use(self, purpose):
        print ("{} đang dừng xe để {}".format(self.name, purpose))
        print ("{} chạy bằng {}".format(self.name, self.material))
    
    def nomay(self):
        print ("{} đang nổ máy".format(self.name))
toyota1 = Toyota("Toyota", "Toyota Hilux", "Đỏ", "Điện")
toyota2 = Toyota("Toyota", "Toyota Yaris", "Vàng", "Deisel")
toyota3 = Toyota("Toyota", "Toyota Vios", "Xanh", "Gas")
toyota1.use("nạp điện")
toyota2.chayxe()
toyota3.nomay()