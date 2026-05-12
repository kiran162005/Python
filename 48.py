# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe = Form

# TWO WAYS TO ACHIEVE POLYMORPHISM

# 1. Inheritance = An object could be treated as the same type as a parent class
# 2. Duck typing = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    

