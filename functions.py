#Functions
#basic func
def myfunc():
    print('Hello World')

#function with arguments
def add(a,b):
    print(a+b)

#function return values
def square(x):
    return x*x

#function with default value of argument
def mult(a,b=5):
    print(a*b)

def subtract(a,b=3):
    print(a - b)
#function with variable number of arguments
def multiadd(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#different way access
myfunc()    
print(myfunc)  
print(myfunc()) 
myfunc
#print(add(10,4)) #This print None Because it print itself in function
add(10,4)
sq =square(10)
print(sq)

#it takes one args and another process with default value.
mult(5)
mult(3,5)
#if you give two argument then it use those otherwise by default values used likw above 
mult(10,4)

#mult(z=10,v=8) #this is not work
mult(b=1,a=2)
print('subtract: ',end=" ")
subtract(b=5,a=2)
print('Function With MultiArguments: ')
#function with multiArguments 
res = multiadd(1)
print(res)
res1 =multiadd(1,2)
print(res1)
res2 =multiadd(1,2,3,4)
print(res2)

#Note: Python Execute Program using Top Down Aproach
#So this is not work
#NameError: name 'printHello' is not defined
#if __name__ == "__main__":
#    printHello()

#def printHello():
#    print("Hello World")
