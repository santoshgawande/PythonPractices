from dictionaries import __dict__
#dictionary are mutable object so it can be modified 
# but keys are always immutable and unique in dictionary.
dict1 = {"key" : "value","name":"san","age":20}
print("original dictionary: ", dict1)

print(dict1['name'],"\n")

#always use 'in' for access dictinary 
for key in dict1 :
    print(dict1[key])

#both key and vallue can be access using enumerate()
for key,value in enumerate(dict1):
    print(key,value)

#Operations :
#print list of key only
print(list(dict1))

#del:key:value pair deleted
del (dict1['key'])
print(dict1)

#check key is present or not
print('key' in dict1)

#create dictionary using dict() from sequence of key-value pairs
#print(dict([('man','san'),(2,"two"),(1,'one')]))
#d = dict(one=1,two=2,three=3)

#dictionary comprensions
d1 = {x:x*x for x in (2,3,4,5,6)}
print("dict Comprension: ", d1)
