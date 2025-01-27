#基本操作
import sys
input = sys.stdin.readline
import math
import heapq

#input
dot, linenum = map(int, input().split())
line = [[]for _ in range(dot + 1)]
for _ in range(linenum):
    a, b, c = map(int, input().split())
    line[a].append((b, c))
    line[b].append((a, c))
costlist = [math.inf] * (dot + 1)
costlist[1] = 0
parlist = [0] *(dot + 1)
q = [(0, 1)]

#dik
while q:
    cost, now = heapq.heappop(q)
    costlist[now] = cost

    for i in line[now]:
        nextdot = i[0]
        nextcost = cost + i[1]
        if nextcost < costlist[nextdot]:
            costlist[nextdot] = nextcost
            heapq.heappush(q, (nextcost, nextdot))
            parlist[nextdot] = now

print(dot - 1)
for i in range(2, dot + 1):
    ans = []
    ans.append(i)
    ans.append(parlist[i])
    print(*ans)

