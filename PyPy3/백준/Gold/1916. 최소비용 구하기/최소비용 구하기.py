import sys
input = sys.stdin.readline
import math
dot = int(input())
line = int(input())
linelist = [[]for i in range(dot + 1)]
for i in range(line):
  a, b, c = map(int, input().split())
  linelist[a].append([b, c])

dotlist = [math.inf] * (dot + 1)

start, end = map(int, input().split())

dotlist[start] = 0

import heapq

que = []
heapq.heappush(que, [0, start])

while que:
  cost, now = heapq.heappop(que)
  if cost > dotlist[now]:
    continue
  for i in linelist[now]:
    if dotlist[i[0]] > cost + i[1]:
      dotlist[i[0]] = cost + i[1]
      heapq.heappush(que, [dotlist[i[0]], i[0]])
    else:
      continue

print(dotlist[end])