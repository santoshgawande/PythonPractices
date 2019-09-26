#OOP's Concepts
#Class and Object
#def f() is called method in class and it must have one args 'self' follows by another argument if present. 
class class1:
    #def method1(): TypeError
    def method(self):
        print('class1 method1')
    
    def method2(self ,something):
        print('class1 methiod2:'+something)
    
   # def method3(someText, self):  #This is not work 
    def method3(self,someText):
        print('class1 methiod3:'+someText)

class class2(class1):
    def anotherMethod(self):
        print('class2 anotherMethod')
    
   # def anotherMethod2(mytext): TypeError
    def anotherMethod2(self,mytext):
        print('result: '+mytext)
    
    def method(self):
        class1.method(self)          #call method from class1
        print('Class2 San')


#Create instance of class
#c1 =class1       #This is not work but above works class declaration works
c1 = class1()
c1.method()
c1.method2('Hello World')
c1.method3('Hi class1')
c2 =class2()
#print('class2 Method: ')
c2.anotherMethod()
c2.anotherMethod2('Hi Class2')

#call method from class1
c2.method()

#Make Class as a Object 
def MyFunc(aClass, *args, **kargs):
    return aClass(*args, **kargs)

class Spam():
    def method(self):
        print('Spam Method')

class Person():
    def __init__(self,name,job=None):
        self.name = name
        self.job = job




object1 = MyFunc(Spam)                                   # Make a Spam object
object2 = MyFunc(Person,'Santosh','Software Engineer')   # Make a Person object
object3 = MyFunc(Person,name='San')                     # Ditto, with keywords and default

#print(object1)
object1.method()
print(object2.name+" "+object2.job)
print(object3.name,object3.job)