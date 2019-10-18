#class examples

class Employee():
    pass

obj1 =Employee()
obj2 = Employee()

#instatiate of class manually
obj1.name ='San'
print(obj1.name)

#method must have self args in class
class Emp():
    def __init__(self,first,last):
        #instant variables
        self.first = first
        self.last = last
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 = Emp('Test','User')
print(emp1.first)

print(emp1.fullname())

print(Emp.fullname(emp1))




