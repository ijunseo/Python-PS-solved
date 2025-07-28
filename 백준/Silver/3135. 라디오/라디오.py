import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
 
lst = []
for _ in range(n):
	lst.append(int(input()))
 
mi = 1001
piv = 0
for i in lst:
    num = abs(i - b)
    if mi > num:
        mi = num
        piv = i
 
print(min(abs(a - b), (abs(piv - b) + 1)))