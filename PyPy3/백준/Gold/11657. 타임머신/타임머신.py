import sys
import math
input = sys.stdin.readline

#基本操作
dot, linenum = map(int, input().split())
line = [[]for _ in range(dot + 1)]
for _ in range(linenum):
	st, de, cst = map(int, input().split())
	line[st].append((de, cst))
timelist = [math.inf] * (dot + 1)
timelist[1] = 0

#ベルマン–フォード法
for i in range(dot):
	for now in range(1, dot + 1):
		for next, cost in line[now]:
			if timelist[now] != -math.inf and timelist[next] > timelist[now] + cost:
				timelist[next] = timelist[now] + cost
				if i == dot - 1:
					print('-1')
					sys.exit()
for i in range(2, dot + 1):
	print(timelist[i] if timelist[i] != math.inf else '-1')