import sys
input = sys.stdin.readline
import math
dot = int(input())
linenum = int(input())
dplist = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
for i in range(1, dot + 1):
    dplist[i][i] = 0
for _ in range(linenum):
    srt, des, cst = map(int, input().split())
    dplist[srt][des] = min(dplist[srt][des], cst)

for k in range(1, dot + 1):
    for i in range(1, dot + 1):
        for j in range(1, dot + 1):
            if dplist[i][j] > dplist[i][k] + dplist[k][j]:
                dplist[i][j] = dplist[i][k] + dplist[k][j]

for i in range(1, dot + 1):
    nowlist = dplist[i]
    anslist = []
    for j in range(1, dot + 1):
        if nowlist[j] == math.inf:
            anslist.append(0)
        else:
            anslist.append(nowlist[j])
    print(*anslist)