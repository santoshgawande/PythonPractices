# Slicing 
#a[m:n] returns the portion of a from index m to, but not including, index n

# Slicing on List :
b = [1,2,3,4,5,6,7,8,9]
print(b[2:6])

# Slicing on String
str1 = ['bar','man','san','pan','ran','aan','bat','cat']
print(str1[2:5])
#reverse slicing 
print(str1[-5:-2])

# slice start beginning of list
b = [2,3,4,5,6,7,8,9]
print(b)
#both are same
print(b[:4], b[0:4])
print(b[2:], b[2:len(b)])

#concatenate slice
c = b[:3] + b[3:]
print(c)

#specify stride either positive or negative
print(b[0:4:2])
print(b[6:0:-2])

#Reverse List or String
print(b[::-1])
print(str1[::-1])

#[:] works different in string and list
#In string it will reference same object but in List it new create copy of that object.
list2 = [33,45,66,77,88,99]
str2  = 'santosh'
temp2 = list2[:]
stemp2 = str2[:]
#list
print('reference of object in slice')
print(list2 is temp2)
#string
print(stemp2 is str2)

# insert element in list without removing anything
# z[n:n] means zero length slice
z = [1,2,7,9]
z[2:2] = [3,4,5,6]
print(z)

# We can delete no of element in middle of list just assigning empty list or use del 
x = [1,2,3,99,55,44,666,4,5,6,7,8]
y = x[:]
x[3:7] = []
print('using slice:',x)
del y[3:7]
print('using del:',y)
