set = {6,8,9,4,3,6,7,3,0}
print(set)
set1 = {3,7,4,9,2,8,5,1}
print(set1)

# Operation

#Intersection
print(set.intersection(set1))
print(set & (set1))

#Union
print(set.union(set1))
print(set | (set1))

# Difference
print(set.difference(set1))
print(set - (set1))

# Symmetric Difference
print(set.symmetric_difference(set1))
print(set ^ set1)

# Superset
su = {2,4,1}
print(set.issuperset(set1))
print(set <= set1)

# Subset
print(su.issubset(set1))
print(su >= set1)

# disjoint set
print(su.isdisjoint(set1))


# Existing Check

print(2 in {1,2,3})
print(4 not in {1,2,3})

# Add or Remove Element in set
s1 = {1,6,3,4,8,4,3}
print(s1)
s1.add(2)
print(s1)
s1.discard(8)
print(s1)
s1.remove(4)
print(s1)

su ={4,5,8,7}
#This is not work but follows line work. because update only works for set of elements
#su.update(1)  
su.update({1})
su.update({2,3})

# If you want to get unique element from list then set is best option for that solution.

# Frozen Set : It can be hashable but set are not hashable
fr = frozenset({5,8})
print(fr.__hash__())

set = {8,7,9}
#print(set.__hash__())

s1 = {7, 'i', 90, 'santosh'}
print(s1)

