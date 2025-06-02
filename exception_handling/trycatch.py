#try catch for Exception Handling
def fetch(obj,index):
    obj =[]
    return obj[index]

def catchException(index):
    try:
        fetch('x',index)
    except IndexError:
        print("Exception",IndexError)
    print('Continue')

catchException(1)
catchException(2)
