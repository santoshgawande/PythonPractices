#program to accept string and print no. of digit and character present in string.

str1 = input('enter string: ')
digit = 0
alpha = 0
for c in str1:
  if c.isdigit():
    digit += 1
  elif c.isalpha() :
    alpha +=1
  else: 
    pass
print('Letter: {}\nDigit: {}'.format(alpha,digit))

