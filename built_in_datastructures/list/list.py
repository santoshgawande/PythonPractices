#!bin/python3
#List : is mutable and it contains complex objects like functions, classes, and modules 
list1 = [11,22,13,1,2,3,4,5,6,7,8,9,10]
print('list')
print(list1)

#List may contains functions, classes and modules etc
def foo():
    pass

import math

a = [int, len, foo, math]
print('func and class and models of list')
print(a)

# Slicing on List : a[m:n] returns the portion of a from index m to, but not including, index n
b = [1,2,3,4,5,6,7,8,9]
print('original list',b)
print('slicing')
print(b[2:6])
#b[1] and b[1:2] are different assignment
print('original list')
t = b
print(t)
t[1] = [2.2,3.3,4.4]
print(t)
t1 = b
t1[1:4] = [22,33,44,55,66]
print(t1)

# insert element in list without removing anything
# z[n:n] means zero length slice 
z = [1,2,7,9]
print('original list',z)
z[2:2] = [3,4,5,6]
print('insert element using slice')
print(z)

# prepending or appending elements to the list using += concatenation operator
a1 = [3,45,67,7]
print('orig list', a1)
a1 +=[111,122,133,144]
print('adding element using += operator in list')
print(a1)
## Operation
print('List Operation')
#append
list1.append(13)
print(list1)

#insert
list1.insert(1,14)
print(list1)

#remove
list1.remove(14)
print(list1)

#sort
list1.sort()
print(list1)

#index
ind = list1.index(22) #value
print(ind)


#Reverse
list1.reverse()
print(list1)

#del
del list1[1]
print(list1)

#copy : it will create shallow copy of list
# it will present in only python3 or greater version
l1 = [1, 23, 4, 5, 6]
t = l1.copy()
print(l1)
print(l1 is t) #Result : False because it is new object of or shallow copy

print(l1 == t) #Result : True because it is same element list 


#clear : it is present in only python3 or greater version
list1.clear()
print(list1)

#Check list of List methods
#p =help(list.__contains__) :used to defination
