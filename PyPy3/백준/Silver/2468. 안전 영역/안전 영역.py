#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
mxans = 0

#solve
def find(li, piv):
	a = 0
	q = deque([])
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	for ii in range(n):
		for jj in range(n):
			if not li[ii][jj]:
				a += 1
				q.append([ii, jj])
				while q:
					nx, ny = q.popleft()
					if li[nx][ny]:
						continue
					li[nx][ny] = 1
					for i in range(4):
						nex = nx + dx[i]
						ney = ny + dy[i]
						if 0 <= nex < n and 0 <= ney < n:
							if not li[nex][ney]:
								q.appendleft([nex, ney])
	return(a)
	
	

for i in range(0, 101):
	llst = [[0]* n for _ in range(n)]
	for j in range(n):
		for k in range(n):
			if lst[j][k] <= i:
				llst[j][k] = 1
	mxans = max(mxans, find(llst, i))
print(mxans)