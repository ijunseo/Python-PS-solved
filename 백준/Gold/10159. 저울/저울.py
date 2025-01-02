import sys
import math
input = sys.stdin.readline
dot = int(input())
linenum = int(input())
line = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
for _ in range(linenum):
    a, b = map(int, input().split())
    line[a][b] = 1
for j in range(1, dot + 1):
    for i in range(1, dot + 1):
        for k in range(1 , dot + 1):
            if line[i][k] > line[i][j] + line[j][k]:
                line[i][k] = line[i][j] + line[j][k]
for i in range(1, dot + 1):
    line[i][i] = 0
for i in range(1, dot + 1):
    ans = 0
    for j in range(1, dot + 1):
        if line[i][j] == line[j][i] == math.inf:
            ans += 1
    print(ans)