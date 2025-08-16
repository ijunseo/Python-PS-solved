import sys 
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

llst = [[1000] * m for _ in range(n)]


dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
lllst = []

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            lllst.append((0, i, j))

while lllst:
    c, x, y = heapq.heappop(lllst)
    if c >= llst[x][y]:
        continue
    llst[x][y] = c
    for k in range(8):
        nc = c + 1
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < n and 0<= ny < m:
            if llst[nx][ny] > nc:
                heapq.heappush(lllst, (nc, nx, ny))

print(max(map(max, llst)))