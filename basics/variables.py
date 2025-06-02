#Variable
f= 10
s ='hello '

#print(s+10) :two different varible can't add 
print(s +str(f))

#re-declaring varibles works
f = 'def'
print(f)

# Global vs. local variables in functions
def myfunc():
    #global f
    f ='Hi'
    print(f)

myfunc()

#Delete varible 
del f
#print (f) : this is not work

#Varible rules 
Var = 'Heruku'
_var1 ='Aws'
#LongestVarible but its works
#Var-1 ='GCP' #this is not work
#1Var ='GCP' #This is not work
#LongestVariable : Python Support Very Long Length for Varible But it causes Performance Issues So but you can write para as a varible. See ex: Varible.txt file 
LongVariable = "Longest Variable Size"
print(LongVariable)
print(Var)
print(_var1)