import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]
llst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(lst[i][j] + llst[i][j], end=' ')
    print()