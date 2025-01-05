import sys
import math
from heapq import *
input = sys.stdin.readline
dot = int(input())
line = [[] for _ in range(dot + 1)]

imsilist = [[math.inf] * (dot + 1)]
for i in range(1, dot + 1):
    nowlist = [math.inf] * (i + 1) + list(map(int, input().split()))
    imsilist.append(nowlist)
que = []
cnt = 0
for i in range(1, dot + 1):
    heappush(que, [imsilist[1][i], 1, i])

wentcheck = [False] * (dot + 1)
wentcheck[1] = True
while cnt != dot - 1:
    _, st, ed = heappop(que)
    if wentcheck[st] == wentcheck[ed] == True:
        continue
    elif wentcheck[st] == False:
        line[st].append(ed)
        line[ed].append(st)
        cnt += 1
        wentcheck[st] = True
        for i in range(1, dot + 1):
            heappush(que, [imsilist[st][i], st, i])
            heappush(que, [imsilist[i][st], st, i])
    elif wentcheck[ed] == False:
        line[st].append(ed)
        line[ed].append(st)
        cnt += 1
        wentcheck[ed] = True
        for i in range(1, dot + 1):
            heappush(que, [imsilist[ed][i], ed, i])
            heappush(que, [imsilist[i][ed], ed, i])


for i in range(1, dot + 1):
    nowlinelist = []
    for j in line[i]:
        nowlinelist.append(j)
    print(len(nowlinelist), *sorted(nowlinelist))