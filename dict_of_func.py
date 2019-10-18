#Python doesn't have switch case
#emulating switch case with dictionary and first-class functions
#fun_dict = {
#    'cond_a' : handle_a,
#    'cond_b' : handle_b,
#}

#if cond == 'cond_a':
#    handle_a()
#elif cond == 'cond_b':
#    handle_b()
#else:
#    handle_default()

def myfunc(a,b):
    return a + b

sum = myfunc(4,5)
print('simple call func: {}'.format(sum))
#first-class functions
funcs =[myfunc]
s = funcs[0](2,3)
print('first-class func :{}'.format(s))

