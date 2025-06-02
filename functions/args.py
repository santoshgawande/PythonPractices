def inp(f_arg, *argv):
    print("first args,",f_arg)
    for arg in argv:
        print('l',arg)

inp('hello','hi','k','l')
