import sys
input = sys.stdin.readline
import math
import heapq

testcase = int(input())

def dijkstra(start):
    que = []
    heapq.heappush(que, [0, start])
    costlist = [math.inf] * (n + 1)
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

for _ in range(testcase):
  n, d, c = map(int, input().split())
  road = [[] for _ in range(n + 1)]
  for i in range(d):
    c1, c2, cst = map(int, input().split())

    road[c2].append([c1, cst])
  anslist = dijkstra(c)
  ans = []
  for i in range(n + 1):
    if anslist[i] == math.inf:
      continue
    else:
      ans.append(anslist[i])
  #print(anslist)
  ans1 = len(ans)
  ans2 = max(ans)
  print(ans1, ans2)




