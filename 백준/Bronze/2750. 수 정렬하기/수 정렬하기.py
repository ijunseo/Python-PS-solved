#基本操作
import sys
input = sys.stdin.readline

#input
n = int(input())
lst = []
for _ in range(n):
    now = int(input())
    lst.append(now)
lst.sort()
for i in lst:
    print(i)