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

#inherited class 
class Developer(Employee):
  pass

emp1 = Employee('san','gawande', 500000)
print(emp1.fullname())
#inherited class
dev1 =Developer('ram','g', 600000)
print(dev1.fullname())

#method resolution
print(help(Developer))

