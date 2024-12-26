import itertools
num = int(input())
numlist = []
for i in range(num):
  numlist.append(i + 1)
exlist =  list(itertools.permutations(numlist, num))
for i in exlist:
  for j in i:
    print(j, end = ' ')
  print()
