import sys
input =sys.stdin.readline
from collections import deque

#input
n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

onelen = [0] * n
twolen = [0] * n
for i in range(1, n):
    now = abs(lst[i][1] - lst[i - 1][1]) + abs(lst[i][0] - lst[i - 1][0])
    onelen[i] = now
for i in range(2, n):
    now = abs(lst[i][1] - lst[i - 2][1]) + abs(lst[i][0] - lst[i - 2][0])
    twolen[i] = now
mx = 0
piv = 0
for i in range(2, n):
    gap = onelen[i] + onelen[i - 1] - twolen[i]
    if gap > mx:
        mx = gap
        piv = i
print(sum(onelen) - onelen[piv] - onelen[piv - 1] + twolen[piv])