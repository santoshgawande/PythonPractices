#!/bin/python3
class Employee:
  raise_amt =1.04
  
  def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
  
  def fullname(self):
      return '{} {}'.format(self.first, self.last)
  
  def apply_raise(self):
      self.pay = int(self.pay * self.raise_amt)

#inherited class from employee
#or subclass
class Developer(Employee):
  def __init__(self, first, last, pay, prog_lang):
      #Employee.__init__(self, first, last, pay)
      #inherited from employee 
      super().__init__(first, last, pay)
      self.prog_lang = prog_lang

class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
      super().__init__(first, last, pay)
      if employees is None:
         self.employees = []
      else : 
         self.employees = employees
  
  def add_emp(self, emp):
      if emp not in self.employees:
         self.employees.append(emp)
  
  def remove_emp(self, emp):
      self.employees.remove(emp)
  
  def print_emps(self):
      for emp in self.employees:
          print('-->', emp.fullname())

    
emp1 = Employee('san','gawande', 500000)
print(emp1.fullname())
#inherited class
dev1 =Developer('ram','g', 600000, 'Python')
dev2 =Developer('san','g', 5600000, 'Python3')

mgr = Manager('su','root', 900000, [dev1, dev2])


print(mgr.fullname())
print(mgr.print_emps())

#isinstance
print(isinstance(mgr, Developer))

#issubclass
print(issubclass(Manager, Employee))



