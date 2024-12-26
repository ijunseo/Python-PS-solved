import sys
num = int(sys.stdin.readline())
numlist = []
for i in range(num):
  a = int(sys.stdin.readline())
  if a != 0:
    numlist.append(a)
  if a == 0:
    numlist.pop()
print(sum(numlist))