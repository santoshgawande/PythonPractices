#accumelate addition
# input : [1, 2, 3, 4, 5]
#output : [1, 3, 6, 10, 15]

def add1(list1):
    addlist = []
    sum = 0
    for ele in list1:
        sum = sum + ele 
        addlist.append(sum)
    return addlist

l1 = [1,2,3,4,5]
add = add1(l1)
print(add)