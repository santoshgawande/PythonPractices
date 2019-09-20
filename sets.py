#Sets misconceptions 
set1 = (1,2,3)  # tuples 
print(set1)
print(type(set1))

#Set : It remove duplicate entries if present.
set2 = {1,3,3,2,4,5,6}
print(set2)
print(type(set2))

#Another way to declare sets
set3 =set({1,2,3,5,5,5,5,6,7,8})
print(set2)

#Set Operation : Union, Intersection, difference, Symmetric Difference
print("diff",set2 - set3)
print("diff",set3 - set2)
print("Union", set2 | set3)
print("Intersection :",set2 & set3)
print("Cartision Product",set2 ^ set3)

#ListComprension are also supported
listCompSet = {x for x in 'aghjsdfghkjhgf' if x not in 'fgjkjh'}
print(listCompSet)