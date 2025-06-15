import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            st = [i, j]

anslst = [[10 ** 7] * m for _ in range(n)]

anslst[st[0]][st[1]] = 0

q = deque([(st[0], st[1])])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    nowx, nowy = q.popleft()
    nowscore = anslst[nowx][nowy]

    for i in range(4):
        nextx = nowx + dx[i]
        nexty = nowy + dy[i]

        if 0 <= nextx < n and 0 <= nexty < m:
            if not lst[nextx][nexty]:
                continue

            if nowscore + 1 < anslst[nextx][nexty]:
                anslst[nextx][nexty] = nowscore + 1
                q.append((nextx, nexty))
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            anslst[i][j] = 0

for i in range(n):
    for j in range(m):
        print(anslst[i][j] if anslst[i][j] != 10 ** 7 else '-1', end = ' ')
    print()