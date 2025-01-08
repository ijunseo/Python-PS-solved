import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
row, col = map(int, input().split())
qmap = [list(map(int, input().split())) for _ in range(row)]
amap = [[-1] * col for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    if x == row - 1 and y == col - 1:
       return 1
    if amap[x][y] != -1:
       return amap[x][y]
    ans = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < row and 0 <= ny < col:
            if qmap[x][y] > qmap[nx][ny]:
                ans += dfs(nx, ny)
    amap[x][y] = ans
    return amap[x][y]
print(dfs(0, 0))