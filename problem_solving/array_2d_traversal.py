#write program which takes two digits m(row) and n(col) as an input and generate 2 dimensional array.
m = int(input('Number of row '))
n = int(input('Number of column '))
arr = []
row = []
for i in range(0, m):
  for j in range(0, n):
     row.append(i*j)
  arr.append(row)
  row = []

print(arr)

