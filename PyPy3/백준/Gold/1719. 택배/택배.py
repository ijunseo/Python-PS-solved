import sys
input = sys.stdin.readline
import math

dot, linenum = map(int, input().split())
line = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
anslist = [[0] * (dot + 1) for _ in range(dot + 1)]

for _ in range(linenum):
  dot1, dot2, cst = map(int, input().split())
  line[dot1][dot2] = cst
  line[dot2][dot1] = cst
  anslist[dot1][dot2] = dot2
  anslist[dot2][dot1] = dot1
for i in range(1, dot + 1):
  line[i][i] = 0
  anslist[i][i] = math.inf
for j in range(1, dot + 1):
  for i in range(1, dot + 1):
    for k in range(1, dot + 1):
      if line[i][k] > line[i][j] + line[j][k]:
        line[i][k] = line[i][j] + line[j][k]
        anslist[i][k] = anslist[i][j]
for i in range(1, dot + 1):
	ansline = []
	for j in range(1, dot + 1):
		if anslist[i][j] == math.inf:
			ansline.append('-')
			continue
		ansline.append(anslist[i][j])
	print(*ansline)