import sys
import math
num = int(sys.stdin.readline())
numlist = []
numlist_L = [[0] * num for i in range (num)]
for i in range(num):
  numlist_L[i][i] = 1
for i in range(num):
  numlist.append(list(map(int, sys.stdin.readline().split())))
for i in range(num - 1):
  if numlist[i][i] == 0:
    print("-1")
    sys.exit()
  for j in range(i + 1, num):
    if numlist[j][i] == 0:
      continue
    else:
      quo = numlist[j][i] / numlist[i][i]
      numlist_L[j][i] = quo
      for k in range(num):
        numlist[j][k] -= quo * (numlist[i][k])
for i in range(num):
  for j in range(num):
    print("{:.3f}".format(numlist_L[i][j]), end=" ")
  print()
for i in range(num):
  for j in range(num):
    print("{:.3f}".format(numlist[i][j]), end=" ")
  print()