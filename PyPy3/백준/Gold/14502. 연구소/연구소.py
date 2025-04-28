import sys
import copy
input = sys.stdin.readline

#input
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
virus_locate = []
for i in range(n):
	for j in range(m):
		if lst[i][j] == 2:
			virus_locate.append([i, j])

#solve
def bfs(inp_virus, inp_map):
	q = inp_virus
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	while q:
		now_r, now_c = q.pop()
		for i in range(4):
			next_r = now_r + dx[i]
			next_c = now_c + dy[i]
			if 0<= next_r < n and 0<= next_c < m:
				if not inp_map[next_r][next_c]:
					inp_map[next_r][next_c] = 2
					q.append([next_r, next_c])
					
	ans = 0
	
	for i in range(n):
		for j in range(m):
			if inp_map[i][j] == 0:
				ans += 1
	return ans
real_ans = 0

def build(now_map, build_num):
	global real_ans
	if build_num == 3:
		bfs_map = copy.deepcopy(now_map)
		bfs_vir = copy.deepcopy(virus_locate)
		real_ans = max(real_ans, bfs(bfs_vir, bfs_map))
		return
	for i in range(n):
		for j in range(m):
			if not now_map[i][j]:
				now_map[i][j] = 1
				build(now_map, build_num + 1)
				now_map[i][j] = 0

build(lst, 0)
print(real_ans)