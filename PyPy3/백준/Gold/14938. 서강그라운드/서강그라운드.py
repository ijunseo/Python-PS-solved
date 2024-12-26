import sys
input = sys.stdin.readline
dot, ran ,linenum = map(int, input().split())
itemlist = [0] + list(map(int, input().split()))
import math
line = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
for i in range(1, dot + 1):
	line[i][i] = 0
for _ in range(linenum):
  st, ne, cst = map(int, input().split())
  line[st][ne] = cst
  line[ne][st] = cst

for k in range(1, dot + 1):
  for i in range(1, dot + 1):
    for j in range(1, dot + 1):
      line[i][j] = min(line[i][j], line[i][k] + line[k][j])
anslist = [0] * (dot + 1)
for i in range(1, dot + 1):
  nowline = line[i]
  for j in range(1, dot + 1):
    if nowline[j] <= ran:
      anslist[i] += itemlist[j]
print(max(anslist))