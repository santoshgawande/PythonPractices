#For loop : If we know how much loop will run then used 
for i in range(5):
    print(i)

#print('\n') #extra just see proper output
#For using String 
for  letter in 'Names':
    print(letter, end =" ")

print('\n')
#For using List sequence : 
# This is the better way about performance than using index

list1 = [1,2,3,'hello']
for l in list1:
    print(l, end=" ")

print('\n')

# using List index
list2 =[1,3,4,56,7,8,90,'hjk',5.6]
for i in range(len(list2)):
    print(list2[i], end=" ")

print('\n')

#enumerate() : used to access element and index of the list at the same time.
list3 = [1,4,5,6,7,'hi','hello','g']
for i,ele in enumerate(list3):
    print(i,ele, end=" ")

print('\n')
#For using Range():
for i in range(10):
    print(i,end = " ")
print('\n')

for i in range(1,10):
    print(i, end=" ")

print('\n')
# For using Range(start, end, step=1)
for i in range(1,10,2):
    print(i, end=" ")
print('\nrevese for loop \n')
#For using negative : decrement for loop
for i in range(5, -1, -1):
    print(i, end=' ')

print('\nreverse()')
#For using reversed():
list4 = ['hi',3,4,56,7,8]
for i  in reversed(list4):
    print(i, end=" ")

print('\n')
#For using zip()
list5 = [2,3,6,7,8,9]
list6 = ['hi','hello','good night','morning']

for i,j in zip(list5,list6):
    print(i,j)



