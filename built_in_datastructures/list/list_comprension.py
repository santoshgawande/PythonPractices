#List of square
square = []
for i in range(1,10):
    square.append(i*i)
print("square list",square)

#List using list,map and lambda function
squareListl =list(map(lambda x: x*x ,range(1,10)))
print("squareList usin lambda:\n",squareListl)

#List Comprensions
squareList = [x*x for x in range(1,10)]
print("squareList With Comprension\n:",squareList)
