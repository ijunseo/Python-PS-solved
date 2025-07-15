import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

llst = [-1] * n

for i in range(n):
    ans = lst.index(min(lst))
    llst[ans] = i
    lst[ans] = 1001

print(*llst)