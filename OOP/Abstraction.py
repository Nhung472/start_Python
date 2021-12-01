# Tính trừu tượng
#có thể ẩn tất cả dữ liệu hoặc quy trình không liên quan
#khi có thay đổi hoạt động bên trong 1 hàm thì cũng không ảnh hưởng tới việc bên khác gọi hàm này
class Coffee:
    def __init__(self):
        pass
    @staticmethod
    def grind(coffee):
        return 'grind'

    @staticmethod
    def prepare_milk():
        return 'milk'

    @staticmethod
    def mix_milk_and_coffee(milk, coffee):
        return milk + 'mixed with' + coffee

    def make_coffee(self, coffee):
        grind = self.grind(coffee)
        milk = self.prepare_milk()
        result = self.mix_milk_and_coffee(milk, grind)

        return result

Coffee = Coffee()
a_cup_of_coffee = Coffee.make_coffee('raw_coffee')