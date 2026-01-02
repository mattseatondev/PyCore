from abc import ABC, abstractmethod

class Shape(ABC): # abstract class
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def str_output(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, wd, ht):
        self.wd = wd
        self.ht = ht
    def area(self):
        return self.wd * self.ht
    def perimeter(self):
        return 2 * (self.wd + self.ht)
    def str_output(self):
        return f"""
            Rectangle has:
            Width of {self.wd},
            Height of {self.ht},
            Area of {self.area()},
            Perimeter of {self.perimeter()}
        """
    
rect = Rectangle(10, 10)

print(rect.str_output())