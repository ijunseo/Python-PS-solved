#基本操作
import sys
input = sys.stdin.readline

#bfs
def bfs(nx, ny):
	#元のグラフを修正できるようにglobal
	global lst
	#bfsのためqueueを作成
	q = [[nx, ny]]
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	while q:
		nowx , nowy = q.pop()
		for i in range(4):
			#新しいノードを探索
			nextx = nowx + dx[i]
			nexty = nowy + dy[i]
			#グラフ範囲内のかを確認
			if 0 <= nextx < c and 0 <= nexty < r:
				if lst[nextx][nexty]:
					lst[nextx][nexty] = 0
					q.append([nextx, nexty])
			

#input
testcase = int(input())
for _ in range(testcase):
	ans = 0
	r, c, qnum = map(int, input().split())
	lst = [[0] * r for _ in range(c)]
	for _ in range(qnum):
		x, y = map(int, input().split())
		#白菜があるとこ
		lst[y][x] = 1
	for i in range(r):
		for j in range(c):
			#白菜があったら
			if lst[j][i]:
				bfs(j, i)
				ans += 1
	print(ans)