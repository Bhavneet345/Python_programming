from math import sqrt
class Calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number
    def square_root(self):
        s=sqrt(self.number)
        return s
    @staticmethod
    def greet(name):
        return f"Hello {name}!!"
s=Calculator(25)
print(s.greet("Bhavneet"))
print(s.square())
print(s.cube())
print(s.square_root())

