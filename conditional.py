#Conditional Statement
x, y = 10, 100
# conditional flow uses if, elif, else  
if(x < y):
    st= "x is less than y"
    print(st)
elif (x == y):
    st= "x is same as y"
    print(st)
else:
    st= "x is greater than y"
    print (st)

# conditional statements let you use "a if C else b"
st1 = "x is less than y" if (x < y) else "x is greater than or equal to y"
print (st1)
  

# Python does not have support for higher-order conditionals
# like "switch-case" in other languages