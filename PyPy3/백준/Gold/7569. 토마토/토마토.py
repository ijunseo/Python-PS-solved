#基本操作
import sys
from collections import deque
input = sys.stdin.readline

#input
q = deque([])
m, n, r = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(n)] for _ in range(r)]

for i in range(r):
	for j in range(n):
		for k in range(m):
			if lst[i][j][k] == 1:
				q.append([i, j, k, 0])
ans = 0

#solv
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
	nowk, nowr, nowc, cst = q.popleft()
	for i in range(6):
		nexr = nowr + dx[i]
		nexc = nowc + dy[i]
		nexk = nowk + dz[i]

		if 0 <= nexr < n and 0 <= nexc < m and 0 <= nexk < r:
			if lst[nexk][nexr][nexc] == 0:
				#print(nexk, nexr, nexc)
				lst[nexk][nexr][nexc] = 1
				nexcst = cst + 1
				ans = max(nexcst, ans)
				q.append([nexk, nexr, nexc, nexcst])

for i in range(r):
	for j in range(n):
		if 0 in lst[i][j]:
			print('-1')
			sys.exit()
print(ans)