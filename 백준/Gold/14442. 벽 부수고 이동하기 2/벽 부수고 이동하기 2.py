import sys
from collections import deque
input = sys.stdin.readline

row, col, k = map(int, input().split())

# 그리드(1-index) 그대로 유지
numlist = [['1'] * (col + 1)]
for _ in range(row):
    line = input().strip()
    numlist.append(['1'] + list(line))

# ans_lst: [k+1][row+1][col+1], 방문/거리 겸용 (-1 = 미방문)
ans_lst = [[[-1]*(col + 1) for _ in range(row + 1)] for _ in range(k + 1)]
ans_lst[0][1][1] = 1

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
q = deque([(1, 1, 0)])

# 로컬 바인딩(파이썬 미세 최적화)
grid = numlist
dist = ans_lst
R, C, K = row, col, k
append = q.append
popleft = q.popleft

while q:
    r, c, j = popleft()
    d = dist[j][r][c]

    if r == R and c == C:  # BFS 특성상 최초 도달이 최단
        print(d)
        break

    nr1 = r + 1; nc1 = c
    if nr1 <= R:
        if grid[nr1][nc1] == '0':
            if dist[j][nr1][nc1] == -1:
                dist[j][nr1][nc1] = d + 1
                append((nr1, nc1, j))
        else:  # '1' (벽)
            if j < K and dist[j+1][nr1][nc1] == -1:
                dist[j+1][nr1][nc1] = d + 1
                append((nr1, nc1, j+1))

    nr2 = r - 1; nc2 = c
    if nr2 >= 1:
        if grid[nr2][nc2] == '0':
            if dist[j][nr2][nc2] == -1:
                dist[j][nr2][nc2] = d + 1
                append((nr2, nc2, j))
        else:
            if j < K and dist[j+1][nr2][nc2] == -1:
                dist[j+1][nr2][nc2] = d + 1
                append((nr2, nc2, j+1))

    nr3 = r; nc3 = c + 1
    if nc3 <= C:
        if grid[nr3][nc3] == '0':
            if dist[j][nr3][nc3] == -1:
                dist[j][nr3][nc3] = d + 1
                append((nr3, nc3, j))
        else:
            if j < K and dist[j+1][nr3][nc3] == -1:
                dist[j+1][nr3][nc3] = d + 1
                append((nr3, nc3, j+1))

    nr4 = r; nc4 = c - 1
    if nc4 >= 1:
        if grid[nr4][nc4] == '0':
            if dist[j][nr4][nc4] == -1:
                dist[j][nr4][nc4] = d + 1
                append((nr4, nc4, j))
        else:
            if j < K and dist[j+1][nr4][nc4] == -1:
                dist[j+1][nr4][nc4] = d + 1
                append((nr4, nc4, j+1))
else:
    # 큐 소진까지 (row,col) 미도달
    print(-1)
