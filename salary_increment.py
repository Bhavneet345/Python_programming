class Employee:
    def __init__(self,salary):
        self.salary=salary
    @property
    def increment(self):
        return self.salary
    @increment.setter
    def change(self,percentage_increase):
        self.salary=((percentage_increase*self.salary)/100)+self.salary
Emp=Employee(100000)
print(Emp.increment)
Emp.change=50
print(Emp.increment)
Emp.salary=12500000
Emp.change=80
print(Emp.increment)
