#While Loop : If you don't know how much loop will iterate then used while.
d =0
while d != 5:
    print(d, end=' ')
    d+=2
print('\n')
#while loop run forever : besically used in server communication.
#while True:
#    print('hello', end=" ")


#while using break statement
c = 0
while True :
    print(c,end =" ")
    c +=1     #because c++ is not work
    if c == 4:
        break  # brek the while loop

print('\n')
#Continue Statement
c1 = 0 
while True :
    print(c1, end=' ')
    c1 +=1
    if c1 != 5:
        continue
    else:
        break