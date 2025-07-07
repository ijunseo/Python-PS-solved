import sys
from collections import deque
import math
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

piv = 0
while True:
	piv += 1
	n = int(input())
	if not n:
		sys.exit()
		
	lst = [list(map(int, input().split())) for _ in range(n)]
	anslst = [[math.inf] * n for _ in range(n)]
	
	q = deque([[0, 0, lst[0][0]]])
	while q:
		nowx, nowy, nowscore = q.popleft() 
		if anslst[nowx][nowy] <= nowscore:
			continue
		anslst[nowx][nowy] = nowscore
		
		for i in range(4):
			nx, ny = nowx + dx[i], nowy + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				nextscore = nowscore + lst[nx][ny]
				if anslst[nx][ny] <= nowscore:
					continue
				q.append([nx, ny, nextscore])

	print('Problem {}: {}'.format(piv, anslst[-1][-1]))