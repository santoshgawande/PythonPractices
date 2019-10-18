#!/bin/python3

#decorator : getter and setter
class Employee:
  
  def __init__(self, first, last):
      self.first = first
      self.last = last
  @property
  def fullname(self):
      return '{} {}'.format(self.first, self.last)

  @fullname.setter
  def fullname(self,name):
      first, last =  name.split(' ')
      self.first = first
      self.last = last
  
  @fullname.deleter
  def fullname(self):
      print('Delete Name')
      self.first = None
      self.last = None

  @property
  def email(self):
      return '{}.{}@email.com'.format(self.first, self.last)

emp1 = Employee('san','gawande')
emp1.fullname = 'Santosh Gawande'
print(emp1.email)

#setter
print(emp1.fullname)

#deleter
del emp1.fullname
print(emp1.fullname)
