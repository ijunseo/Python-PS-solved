#基本操作
import sys
input = sys.stdin.readline

#input
n = int(input())
lst = [input().rstrip() for _ in range(n)]
llst = [[0] * n for _ in range(n)]
piv = 1
pivnum = 1
anslst = []

#bfs
def bfs(start):
	global llst
	global pivnum
	global piv
	q = [start]
	
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	while q:
		nowx, nowy = q.pop()
		for i in range(4):
			nx = nowx + dx[i]
			ny = nowy + dy[i]
			if -1 < nx < n and -1 < ny < n:
				if lst[nx][ny] == '1' and not llst[nx][ny]:
					llst[nx][ny] = piv
					pivnum += 1
					q.append([nx, ny])

#ans
for i in range(n):
	for j in range(n):
		if lst[i][j] == '1' and not llst[i][j] :
			llst[i][j] = piv
			bfs([i,j])
			anslst.append(pivnum)
			piv += 1
			pivnum = 1
			
#output
print(len(anslst))
for i in sorted(anslst):
	print(i)