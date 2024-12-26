import sys
input = sys.stdin.readline
from collections import deque
import math
dot, route_num = map(int, input().split())
road = [[] for i in range(dot + 1)]
for _ in range(route_num):
    dot1, dot2, length = map(int, input().split())
    road[dot1].append([dot2, length])
    road[dot2].append([dot1, length])

dot_1, dot_2 = map(int, input().split())

import heapq
que = []
heapq.heappush(que, [0, 1])
costlist = [math.inf] * (dot + 1)
costlist[1] = 0
while que:
  cost, now = heapq.heappop(que)
  if cost > costlist[now]:
    continue
  for i, j in road[now]:
    newcost = cost + j    
    if costlist[i] > newcost:
      costlist[i] = newcost
      heapq.heappush(que, [newcost, i])

route1_1 = costlist[dot_1]
route2_1 = costlist[dot_2]

que = []
heapq.heappush(que, [0, dot_1])
costlist = [math.inf] * (dot + 1)
costlist[dot_1] = 0
while que:
  cost, now = heapq.heappop(que)
  if cost > costlist[now]:
    continue
  for i, j in road[now]:
    newcost = cost + j    
    if costlist[i] > newcost:
      costlist[i] = newcost
      heapq.heappush(que, [newcost, i])

route1_2 = costlist[dot_2]
route2_2 = costlist[dot_2]
route2_3 = costlist[-1]

que = []
heapq.heappush(que, [0, dot_2])
costlist = [math.inf] * (dot + 1)
costlist[dot_2] = 0
while que:
  cost, now = heapq.heappop(que)
  if cost > costlist[now]:
    continue
  for i, j in road[now]:
    newcost = cost + j    
    if costlist[i] > newcost:
      costlist[i] = newcost
      heapq.heappush(que, [newcost, i])
route1_3 = costlist[-1]

route1 = route1_1 + route1_2 + route1_3
route2 = route2_1 + route2_2 + route2_3
ans = min(route1, route2)
if ans == math.inf:
  print('-1')
else:
  print(ans)