import sys
input = sys.stdin.readline
import math
import heapq

dot, line = map(int, input().split())

def dijkstra(start):#未知のリスト（2次元）をroadにする
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

road = [[]for _ in range(dot + 1)]
for i in range(line):
  cmd = input().strip().split()
  if cmd[0] == '1':
    com, dot1, dot2, cst = map(int, cmd)
    road[dot1].append([dot2, cst])
    road[dot2].append([dot1, cst])
  if cmd[0] == '0':
    com, fir, dest = map(int, cmd)
    anslist = dijkstra(fir)
    ans = anslist[dest]
    if ans == math.inf:
      print('-1')
    else:
      print(ans)
  #print(cmd)
#print(road)