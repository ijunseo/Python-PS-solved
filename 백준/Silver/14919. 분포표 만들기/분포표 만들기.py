import sys
input = sys.stdin.readline

n = int(input())

lst = [i/n for i in range(1, n + 1)]
lllst = [0 for i in range(n)]

import bisect

llst = list(map(float, input().split()))

for i in range(len(llst)):
    now = llst[i]
    rgt = bisect.bisect_right(lst, now)
    lllst[rgt] += 1

for i in lllst:
    print(i, end = ' ')
