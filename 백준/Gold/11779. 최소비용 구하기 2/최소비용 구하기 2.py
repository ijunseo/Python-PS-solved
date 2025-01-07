import sys
input = sys.stdin.readline
import math
import heapq
import copy

dot = int(input())
line = int(input())

def dijkstra(start, end):#未知のリスト（2次元）をroadにする
  que = []
  heapq.heappush(que, [0, start,[]])
  costlist = [[math.inf, []] for _ in range(dot + 1)]#cost, 点の数、訪問した点
  costlist[start][0] = 0
  while que:
    cost, now,wentcity  = heapq.heappop(que)
    if cost > costlist[now][0]:
      continue
    newwentcity = copy.deepcopy(wentcity)
    newwentcity.append(now)
    for i, j in road[now]:
      newcost = cost + j
      if costlist[i][0] > newcost:
        costlist[i][0] = newcost
        costlist[i][1] = newwentcity
        heapq.heappush(que, [newcost, i, newwentcity])
  costlist[end][1].append(end)
  return costlist[end]

road = [[]for _ in range(dot + 1)]
for _ in range(line):
  fir, fin, cst = map(int, input().split())
  road[fir].append([fin, cst])

first , destination = map(int, input().split())
ans = dijkstra(first, destination)
print(ans[0])
print(len(ans[1]))
print(*ans[1])