#Class Variable : same for all instance
# Instance Variable : same only one instance

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
        ##self.pay = int(self.pay * Employee.raise_amount) # it work
        ##but it benenfit if we change instamce raise_amount it will also change
        self.pay = int(self.pay * self.raise_amount)

print(Employee.emp_no)
emp1 = Employee('San','G',60000)
emp2 = Employee('Test','User',50000)
print(Employee.emp_no)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

##access class variable
#print(Employee.raise_amount)
#print(emp1.raise_amount)

##namespace 
#print(emp1.__dict__)
#print(Employee.__dict__)

#print(emp2.pay)
#emp2.apply_raise = 1.05
#print(emp2.pay)




