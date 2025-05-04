import sys
input = sys.stdin.readline
import bisect

n = int(input())
lst = list(map(int ,input().split()))
llst = []

for i in range(n):
    now = lst[i]
    if not llst:
        llst.append(now)
        continue
    if now > llst[-1]:
        llst.append(now)
    elif now < llst[-1]:
        lft = bisect.bisect_left(llst, now)
        llst[lft] = now
print(n - len(llst))