from dictionaries import __dict__
#dictionary are mutable object so it can be modified 
# but keys are always immutable and unique in dictionary.
dict1 = {"key" : "value","name":"san","age":20}
print("original dictionary: ", dict1)

print(dict1['name'],"\n")

#create dict 
d = dict([(1,6),(7,8)])


#always use 'in' for access dictinary 
for key in dict1 :
    print(dict1[key])

#both key and value can be access using enumerate()
for key,value in enumerate(dict1):
    print(key,value)
print('\nkey-value using dict1.items()\n')
#usinf items() we can acces both key-value from dictonary
for k,val in dict1.items():
    print(k,val)
print('\n list of key only from dict \n')

#Operations :
#access 
d2 = {'one' : 1, 'two' : 2}

#access using key
print(d2['one'])
print(d2.get('one'))

#print list of key only
print(list(dict1))

#insert into dict
d1 ={}
d1['h'] = 'hello'

#adding multi value
d['value'] = 1,2,3,4,5
print(d)

#update value
d = {'key' : 'value'}
d['key'] = 'high'
print(d)

#del:key:value pair deleted
del (dict1['key'])
print(dict1)
print('\n')
#check key is present or not
print('key' in dict1)

#create dictionary using dict() from sequence of key-value pairs
#print(dict([('man','san'),(2,"two"),(1,'one')]))
#d = dict(one=1,two=2,three=3)

#dictionary comprensions
d1 = {x:x*x for x in (2,3,4,5,6)}
print("dict Comprension: ", d1)
