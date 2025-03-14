#基本操作
import sys
from collections import deque
input = sys.stdin.readline

#input
q = deque([])
m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
	for j in range(m):
		if lst[i][j] == 1:
			q.append([i, j, 0])
llst = [[0] * m for _ in range(n)]
ans = 0
#solv
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
	nowr, nowc, cst = q.popleft()
	for i in range(4):
		nexr = nowr + dx[i]
		nexc = nowc + dy[i]
		if 0 <= nexr < n and 0 <= nexc < m:
			if lst[nexr][nexc] == 0:
				lst[nexr][nexc] = 1
				nextcst = cst + 1
				llst[nexr][nexc] = nextcst
				q.append([nexr, nexc, nextcst])
for i in range(n):
	if 0 in lst[i]:
		print('-1')
		sys.exit()
mx = 0
for i in range(n):
	mx = max(mx, max(llst[i]))
print(mx)