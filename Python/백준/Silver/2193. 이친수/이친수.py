import sys
num = int(sys.stdin.readline())
numlist = [0, 1]
for i in range(num - 1):
  numlist.append(numlist[i] + numlist[i + 1])
print(numlist[num])