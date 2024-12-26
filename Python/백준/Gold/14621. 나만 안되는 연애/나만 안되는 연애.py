import sys
input = sys.stdin.readline
dot, linenum = map(int, input().split())
schoollist = [False] + list(map(str, input().split()))
line = [[] for _ in range(dot + 1)]
for _ in range(linenum):
  a, b, c = map(int, input().split())
  line[a].append((b, c))
  line[b].append((a, c))
from heapq import *
que = [(0, 1, 0)]
import math
went = [math.inf] * (dot + 1)
while que:
  cst, now, last = heappop(que)
  if went[now] != math.inf or schoollist[last] == schoollist[now]:
    continue
  went[now] = cst
  for next, cost in line[now]:
    if schoollist[now] == schoollist[next] or went[next] != math.inf:
      continue
    heappush(que, (cost, next, now))
if math.inf in went[1:]:
	print('-1')
else:
	print(sum(went[1:]))