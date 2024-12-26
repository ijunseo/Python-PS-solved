import sys
input = sys.stdin.readline
import math
import heapq

dot, line, fir = map(int, input().split())
linelist_1 = [[] for i in range(dot + 1)]
linelist_2 = [[] for i in range(dot + 1)]

for i in range(line):
  a, b, c = map(int, input().split())
  linelist_1[a].append([b, c])
  linelist_2[b].append([a, c])
def dijkstra(start, road):#未知のリスト（2次元）をroadにする
    que = []
    heapq.heappush(que, [0, start])
    costlist = [math.inf] * (dot + 1)
    costlist[start] = 0
    while que:
      cost, now = heapq.heappop(que)
      if cost > costlist[now]:
        continue
      for i, j in road[now]:
        newcost = cost + j    
        if costlist[i] > newcost:
          costlist[i] = newcost
          heapq.heappush(que, [newcost, i])
    return costlist

route_1 = dijkstra(fir, linelist_1)
route_2 = dijkstra(fir, linelist_2)
anslist = []
for i in range(1, dot + 1):
  anslist.append(route_1[i] + route_2[i])
print(max(anslist))