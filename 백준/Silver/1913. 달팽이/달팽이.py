import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

lst = [[0] * n for _ in range(n)]
x , y = n // 2, n // 2

point = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

lst[x][y] = point
point += 1

if m == 1:
    rx, ry = x + 1, y + 1

for i in range(1, x + 1):
    if point == 2:
        nx, ny = x - 1, y - 1
    else:
        nx, ny = nx - 1, ny - 1
    
    step = i * 2
    for j in range(4):
        for k in range(step):
            nx = nx + dx[j]
            ny = ny + dy[j]
            lst[nx][ny] = point
            if point == m:
                rx, ry = nx+1, ny+1
            point += 1

for i in lst:
    print(*i)
print(rx, ry)