#accept name and age and print that user age will be 100yrs in this year
import datetime

curr =datetime.date.today()
#print(curr.year)
name = input('enter name: ')
age = int(input('enter age: '))
rem = 100 - age
#print(rem)
fyear = int(curr.year) + rem 
print('{} will be 100yrs old in the year: {}'.format(name,fyear))                      
