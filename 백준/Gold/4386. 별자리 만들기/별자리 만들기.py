import sys
import math
input = sys.stdin.readline
dot = int(input())
from heapq import *
dotlist = []
for _ in range(dot):
    now = list(map(float, input().split()))
    dotlist.append(now)
wentcheck = [False] * dot
wentcheck[0] = True
que = []
def dis(a, b):
    a0, a1 = dotlist[a][0], dotlist[a][1]
    b0, b1 = dotlist[b][0], dotlist[b][1]
    return (math.sqrt((a0 - b0) ** 2 + (a1 - b1) ** 2))
for i in range(dot):
    heappush(que, [dis(0, i), i])
ans = 0
while que:
    dist, quedot = heappop(que)
    if wentcheck[quedot] == True:
        continue
    wentcheck[quedot] = True
    ans += dist
    for i in range(dot):
        if wentcheck[i] == True:
            continue
        else:
            heappush(que, [dis(quedot, i), i])
print(round(ans, 3))