#基本操作
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10** 6)

#input
q = []
m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
	for j in range(m):
		if lst[i][j] == 1:
			q.append([i, j])
ans = 0
#solv
def solv(now):
	global ans
	global lst
	q_now = []
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	while now:
		nowr, nowc = now.pop()
		for i in range(4):
			nexr = nowr + dx[i]
			nexc = nowc + dy[i]
			if 0 <= nexr < n and 0 <= nexc < m:
				if lst[nexr][nexc] == 0:
					lst[nexr][nexc] = 1
					q_now.append([nexr, nexc])
	if q_now:
		ans += 1
		solv(q_now)
				
solv(q)
for i in range(n):
	for j in range(m):
		if lst[i][j] == 0:
			print('-1')
			sys.exit()
#output
print(ans)