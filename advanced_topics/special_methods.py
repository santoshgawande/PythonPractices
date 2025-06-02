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

  def __repr__(self):
      return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)
  
  def __str__(self):
      return '{} - {}'.format(self.fullname(), self.pay)

  def __add__(self, other):
      return self.pay + other.pay

  def __len__(self):
      return len(self.fullname())

emp1 = Employee('san','gawande', 500000)
emp2 = Employee('ram','g', 680000)
#special method used for operator overloading
print(emp1.__repr__())
print(emp1.__str__())
#both works as same

print(repr(emp1))
print(str(emp1))

#it works because of __add__() method otherwise it shows error.
print(emp1 + emp2)
print(len(emp1))
