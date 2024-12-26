import sys
import bisect
from itertools import *
input = sys.stdin.readline

num, target = map(int, input().split())
numlist = list(map(int, input().split()))
half_num = num // 2
lftlist = numlist[:half_num]
rgtlist = numlist[half_num:]

Lft = []
Rgt = []

for i in range(1, half_num + 1):
    for j in combinations(lftlist, i):
        Lft.append(sum(j))
#print(Lft)

for i in range(1, num - half_num + 1):
    for j in combinations(rgtlist, i):
        Rgt.append(sum(j))
#print(Rgt)

Rgt.sort()
#print(Rgt)

cnt = 0
for i in Lft:
    ans = target - i
    leftindex = bisect.bisect_left(Rgt, ans)
    rightindex = bisect.bisect_right(Rgt, ans)
    cnt += rightindex - leftindex

cnt += Rgt.count(target)
cnt += Lft.count(target)
        
print(cnt)