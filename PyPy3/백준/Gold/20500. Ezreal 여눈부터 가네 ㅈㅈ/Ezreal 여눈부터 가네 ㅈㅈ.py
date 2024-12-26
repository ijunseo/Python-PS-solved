import math
import sys
num = int(input())
numlist = [0, 1, 1, 3]
if num < 5:
    print(numlist[num - 1])
    sys.exit()
for i in range(4, num):
    numlist.append((numlist[i - 1] + (numlist[i - 1] - numlist[i - 2]) + 2 * (numlist[i - 2] - numlist[i - 3])) % 1000000007)
print(numlist[-1] % 1000000007)