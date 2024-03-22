print(type(["a"]))

class Circle():
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r

C1 = Circle(10, 'Red')
print(C1.radius)

BlueCircle=Circle(10,'blue')
BlueCircle.add_radius(20)
print(BlueCircle.radius)

import matplotlib.pyplot as plt
  
# Create a class Circle
class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
#print(dir(RedCircle))

print(RedCircle.radius)
print(RedCircle.color)

RedCircle.radius = 1
print(RedCircle.radius)

#draw circle
#print(RedCircle.drawCircle())

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)
print(BlueCircle.radius)
print(BlueCircle.color)
#print(BlueCircle.drawCircle())

# Create a new Rectangle class for creating a rectangle object
class Rectangle(object):
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
print(SkinnyBlueRectangle.height)
print(SkinnyBlueRectangle.width)
print(SkinnyBlueRectangle.color)
#print(SkinnyBlueRectangle.drawRectangle())

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')
print(FatYellowRectangle.height)
print(FatYellowRectangle.width)
print(FatYellowRectangle.color)
#print(FatYellowRectangle.drawRectangle())

##VEHICLES
class Vehicles(object):
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)
vehicle1 = Vehicles(200, 20)
vehicle1.assign_seating_capacity(5)
print(vehicle1.display_properties())

vehicle2 = Vehicles(180, 25)
vehicle2.assign_seating_capacity(4)
print(vehicle2.display_properties())

