import sys
input = sys.stdin.readline
import math
dot = int(input())
linenum = int(input())
linelist = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
nextlist = [[math.inf] * (dot + 1) for _ in range(dot + 1)]

for i in range(1, dot + 1):
    linelist[i][i] = nextlist[i][i] = 0

for _ in range(linenum):
    st, de, cst = map(int, input().split())
    if cst < linelist[st][de]:
        linelist[st][de] = cst
        nextlist[st][de] = de

for j in range(1, dot + 1):
    for i in range(1 , dot + 1):
        for k in range(1, dot + 1):
            if linelist[i][k] > linelist[i][j] + linelist[j][k]:
                linelist[i][k] = linelist[i][j] + linelist[j][k]
                nextlist[i][k] = nextlist[i][j]

for i in range(1, dot + 1):
    for j in range(1, dot + 1):
        if linelist[i][j] == math.inf:
            linelist[i][j] = 0

for i in range(1 , dot + 1):
    nowlist = linelist[i][1:]
    print(*nowlist)

# for i in range(1 , dot + 1):
#     nowlist = nextlist[i][1:]
#     print(*nowlist)

def finddes(st, de):
    global went
    went.append(st)
    if st == de:
        return
    if nextlist[st][de] == 0 or nextlist[st][de] == math.inf:
        went = [0]
        return 
    else:
        nextdot = nextlist[st][de]
        finddes(nextdot, de)

for i in range(1, dot + 1):
    for j in range(1, dot + 1):
        went = []
        finddes(i, j)
        length = len(went)
        if length == 1:
            print('0')
        else:
            print(length, end = ' ')
            print(*went)