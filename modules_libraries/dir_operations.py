#dir() with standard library gives list function and attribute that library provides.
import sys
import os

l = dir(sys)
print('sys fuctions\n',l,'\n')
lf = dir(os)
print('os fuctions \n',lf)

#__doc__ : is present every library and it show documentation about function that present in method
print(os.__doc__)