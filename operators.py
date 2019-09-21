#Operator : + - * / // **
a,b=30,5

print(a*b)

print(a/b)

print(a//b)

print(a-b)

print(a+b)

print(a**5)

print(a%b)

print('\nBoolean Operator:')
#Boolean
c,d = True, False
print(c or d)
print(c & d)
print(c and d)
print(not c)

print('\ncomparison operator :\n')
#Comparison : ==, >, <, != 
e,f = 8, 9
print(c == d)
print(c != d)
print(e > f)
print(e< f)
print(e >=f)

print('\n Bitwise Operator:')
#Bitwise Operator : ex with Higher Precedence
#Bitwise Unary -(num + 1)
print(~a)

#Bitwise Left Shift : a left shifted by b bits
print(a << b)

#Bitwise Right Shift : a right shifted by b bits
print(a >> b)

#Bitwise AND
print(a & b)

#bitwise XOR (exclusive OR)
print(a ^ b) # 27

#Bitwise OR
print(a | b)

#Membership Operator : in , not in
str9 ='sdfghjk;a'
if ';' in str9 :
    print(True)
if 'o'  not in str9 :
    print(False)
