#String : It is immutable data structure so we can't change it after assign the string.
str1 ='This is the string.'
st ="this another representaion"
paragraph =""" This is String Paragraph
   This is 2nd line with customization
   this is 3rd line
   """
print('using single quotes:\t',str1)
print('using double quotes:\t',st)
print("define para using triple quotes:\t",paragraph)

#Access string in different way:
print(str1[0])
print(str1[1:6])
print(str1[1:])

for char in str1 :
    print(char,end =' ')

print('\n')
#using index : basically all like list string can be access. but assignment is not work for string.
for i in range(len(str1)):
    print(str1[i],end =' ')

print('\n Repitation of String:')

#Repitation of string
print(str1*3,end='')

#Update String:
str3 ='Hello '
str4 ='San'
str3 =str3[:6] + str4
print(str3)

#Remove Char from string
str2 = 'Hello World'
print(str2[:2]+str2[3:])

#Delete string we can assign empty string or 'del' keyword to delete it.
str5 ='This is string'
str5 =' '
print('empty string :'+str5)

#del keyword whole object of string.
str6 = 'hello'
#del str6
#print(str6)

print('\nString Comparison :')
#String With Comparison Operators : strings are compared lexicographically (ASCII value order).
str7 ='abc'
str8 ='xyz'

print(str7 > str8)
print(str7 < str8)
print(str7 == str8)
print(str7 != str8)

print('\nMemberShip Operator:')
#Membership Operator : in , not in
str9 ='sdfghjk;a'
if ';' in str9 :
    print(True)
if 'o'  not in str9 :
    print(False)

print('\nString Builtin Functions()')
#String Predefine Module  : standard string functions
str10 ='Hello'

up =str10.upper()
print(up)
print(str10.lower())
print(str10.title())
#c = str10.count()
#import  string : it shows two times next line output  <---------
print(str10.isupper())

#String Only Operators : It is like C language Specifiers
#Integer -> String
print("integer: "+"%+d"%4)
print(type("%+d"%4))

#HexaDecimal -> String
print("HexaDecimal:"+'%0x'%108)

print("octal:\t"+'%o'%307)
#float -> String
print("float:"+'%f'%104.556)

#exponentional -> String 
print("exponential: "+'%e'%102.4567858)

# Raw-String Operators 
print(r'Hello')
f =r'Hello'
print(type(f))

#best example explain this raw-string : it is use in regular expression.
print(r'\n')
print('\n')

#Unicode String
u =u'Hello'
print(u)
print(type(u))

#print(ur"Hello") : This show run time error  <------ ?

#String are immutable so when create string python assign space to string when we 
#concatenate with another string then first space automatic deallocate and assign to anither space.
# using id() we can see exact memory location 
#Both have memory location are different.
st1 ='hello'
print(id(st1))
st1 = st1 + 'World'
print(id(st1))

#assignment not allowed
#st1[0] ='H' #caues error : TypeError: 'str' object does not support item assignment
#Note : Our third fact is that Python does not have an "array" type as a
#primitive (although the array module exists if you really have to have one).
# character is not a type in Python
#Unlike C strings, Python strings do not Terminate with NUL or '\0'
