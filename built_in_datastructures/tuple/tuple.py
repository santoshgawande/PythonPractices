#Tuple are immutable so assignment is not supported
#tuple1[1] = 455 not support

tuple1 = (1,2)
tuple2 = (1,2,3)
print(tuple1)
print(tuple2)

#assign in another way
tuple3 = 1, 4, "hello"
print(tuple3)

#singlton tuple
tuple4 = 'hello',
print(tuple4)

#operation
#len
print(len(tuple4))

#tuple packing and sequence unpacking
x, y, z = tuple2

print(x)
print(y)
print(z)