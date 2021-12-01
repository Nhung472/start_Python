#Tính đóng gói
#đóng gói data lại và kiểm soát việc truy cập và thay đổi data từ bên ngoài
#1 _: internal use (vẫn có thể public access nhưng bị cảnh báo)
#2 __:private (không thể public access)

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self): 
        print("Giá bán sản phẩm: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()