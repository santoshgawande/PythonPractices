#Regular Method : it has first args is a self
#Class method: has first args as 'cls' with decorator as a '@classmethod'
# Static Method : dont pass automatically args or instance they just like function but it is in class

#decorator : it alter the functionallaty of method
class Employee:
    #class Variable
    raise_amount = 1.04
    emp_no = 0
    def __init__(self,first,last,pay):
        #instant variables
        self.first = first
        self.last = last
        self.pay = pay
        Employee.emp_no +=1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    #class Method
    @classmethod
    def apply_raise_amt(cls, amount):
        cls.raise_amount = amount
    #class methpd as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        #create new employee object
        return cls(first,last,pay)
    
    #static method
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday():
            return False
        return True
    

emp1 = Employee('San','G',60000)
emp2 = Employee('Test','User',50000)

##it skip class varible automatically
#emp1.apply_raise_amt(4)
Employee.apply_raise_amt(10)
print(Employee.raise_amount)
print(emp1.raise_amount)

#
emp1_str ='S-G-100000'
new_emp1 = Employee.from_string(emp1_str)
print(new_emp1.first)
print(new_emp1.last)
print(new_emp1.pay)


from datetime import date
mydatetime= date(2019,9,28)
print(Employee.is_weekday(mydatetime))