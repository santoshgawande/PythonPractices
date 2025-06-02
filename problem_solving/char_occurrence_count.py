#No. of Occurence of each word in given string.
def count(str1):
  count = dict()
  words = str1.split()
  for word in words :
    if word in count :
        count[word] += 1
    else :
        count[word] = 1
  return count


str1 = 'india is my country  all indian are my brothers and sister I love my country'

print(count(str1))
