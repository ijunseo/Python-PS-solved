import sys
input = sys.stdin.readline

n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]
llst = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

for i in range(n):
    for j in range(n):
        if lst[i][j] == '.':
            for k in range(8):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if lst[ni][nj].isdigit():
                        llst[i][j] += int(lst[ni][nj])
        else:
            llst[i][j] = '*'

for i in range(n):
    for j in range(n):
        if type(llst[i][j]) == int:
            if llst[i][j] < 10:
                print(llst[i][j], end='')
            else:
                print('M', end='')
        else:
            print('*', end='')
    print()