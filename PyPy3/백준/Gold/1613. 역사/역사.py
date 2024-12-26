import sys
input = sys.stdin.readline
num, linenum = map(int, input().split())
import math
line  =[[math.inf] * (num + 1)for _ in range(num + 1)]
for _ in range(linenum):
    a, b = map(int, input().split())
    line[a][b] = 1
for j in range(1, num + 1):
    for i in range(1, num + 1):
        for k in range(1, num + 1):
            if line[i][k] > line[i][j] + line[j][k]:
                line[i][k] = line[i][j] + line[j][k]
qnum = int(input())
for _ in range(qnum):
    st, ed = map(int, input().split())
    if line[st][ed] == math.inf and line[ed][st] == math.inf:
        print('0')
    elif line[st][ed] == math.inf and line[ed][st] != math.inf:
        print('1')
    elif line[st][ed] != math.inf and line[ed][st] == math.inf:
        print('-1')