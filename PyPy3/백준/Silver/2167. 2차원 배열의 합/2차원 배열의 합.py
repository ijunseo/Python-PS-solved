import sys
import math
num1, num2 = map(int, sys.stdin.readline().split())
numlist = []
for i in range(num1):
    numlist.append(list(map(int, sys.stdin.readline().split())))
num = int(sys.stdin.readline())
for i in range(num):
    a1, a2, b1, b2 = map(int, sys.stdin.readline().split())
    answer = sum(sum(numlist[j][a2 - 1 : b2]) for j in range(a1 - 1 , b1))
    print(answer)