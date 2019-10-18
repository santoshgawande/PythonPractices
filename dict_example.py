#dict trick
d = {True: 'yes', 1: 'no', 1.0: 'maybe' }
print(d)

#It will print {True: 'maybe'}
#why this is happen ? : Because True = 1 = 1.0 are same in python 
res = True == 1 == 1.0
print(res)
