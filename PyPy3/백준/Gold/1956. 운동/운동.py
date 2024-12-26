import sys
input = sys.stdin.readline
dot, linenum = map(int, input().split())
import math
line = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
for i in range(1, dot + 1):
  line[i][i] = 0
for _ in range(linenum):
  start, next, cost = map(int, input().split())
  line[start][next] = cost

for j in range(1, dot + 1):
  for i in range(1, dot + 1):
    for k in range(1, dot + 1):
      line[i][k] = min(line[i][k], line[i][j] + line[j][k])

anslist = [[math.inf] * (dot + 1) for _ in range(dot + 1)]


for i in range(1, dot + 1):
  for j in range(1, dot + 1):
    anslist[i][j] = line[i][j] + line[j][i]
for i in range(1, dot + 1):
  anslist[i][i] = math.inf

ans = math.inf
for i in range(1, dot + 1):
  for j in range(1, dot + 1):
    ans = min(ans, anslist[i][j])
if ans == math.inf:
  print('-1')
  sys.exit()
print(ans)
