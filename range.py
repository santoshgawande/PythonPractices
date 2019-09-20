#range()
list1 = [1,2,45,6,7,8]

#this iterate without using range
print("print list without ange()")
for ele in list1:
   print(ele)

#for using range() in python3 behave exact xrange() in python2.7
# in python3 xrange() merge to range(). it only one element process and print
# but in python2 range() iterate complete list then print so memory it reduced memory uses.

print("print list usin range()")
for ele in range(len(list1)):
    print(ele)
