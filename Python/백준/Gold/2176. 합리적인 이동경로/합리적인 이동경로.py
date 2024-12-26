import sys
input = sys.stdin.readline
import math
import heapq

dot, line = map(int, input().split())
linelist = [[] for _ in range(dot + 1)]
lenlist = [math.inf] * (dot + 1)
wentlist = [0] * (dot + 1)
wentlist[2] = 1
for _ in range(line):
    st, de, cst = map(int, input().split())
    linelist[st].append([de, cst])
    linelist[de].append([st, cst])

def dfs(fir):
    now = fir
    for i, j in linelist[now]:
        if lenlist[i] < lenlist[now]:
            if wentlist[i] == 0:
                dfs(i)
            wentlist[now] += wentlist[i]
def dik(fir):
    que = []
    heapq.heappush(que, (0, fir))
    lenlist[fir] = 0
    while que:
        cost, now = heapq.heappop(que)
        for i, j in linelist[now]:
            nextcost = cost + j
            nextdot = i
            if lenlist[nextdot] > nextcost:
                lenlist[nextdot] = nextcost
                heapq.heappush(que, (nextcost, nextdot))
    dfs(1)
    return(wentlist[1])
    
print(dik(2))
