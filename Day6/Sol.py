import math  # for pi

# Base Class
class Shape:
    def area(self):
        # Base method - to be overridden by subclasses
        return 0


# Derived Class 1 - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Overriding the area() method
    def area(self):
        return self.length * self.width


# Derived Class 2 - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area() method
    def area(self):
        return math.pi * (self.radius ** 2)


# ---- Testing the Classes ----
# Create objects of Rectangle and Circle
rect = Rectangle(10, 5)
circ = Circle(7)

# Call the area() method
print("Area of Rectangle:", rect.area())
print("Area of Circle:", circ.area())
