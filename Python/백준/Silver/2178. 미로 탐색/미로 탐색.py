#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input
n,m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]
q = deque([(0, 0)])
anslst = [[0] * (m) for _ in range(n)]

#bfs
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


while q:
	#row and collumn
	r, c = q.popleft()
	for i in range(4):
		#new_row and new_collumn
		nr = r + dx[i]
		nc = c + dy[i]
		#グラフ範囲内
		if nr < 0 or nc < 0 or nr > n - 1 or nc > m - 1:
			continue
		#原点に戻らないように
		if nr == 0 and nc == 0:
			continue
		#いけないならcontinue
		if lst[nr][nc] == '0':
			continue
		if not anslst[nr][nc]:
			anslst[nr][nc] = anslst[r][c] + 1
			q.append((nr, nc))
print(anslst[-1][-1] + 1)
	
	
	
