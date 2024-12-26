import sys
import math

input = sys.stdin.readline
dot, qu_num = map(int, input().split())
line = [[] for _ in range(dot + 1)]
for _ in range(dot - 1):
    dot1, dot2, len = map(int, input().split())
    line[dot1].append([dot2, len])
    line[dot2].append([dot1, len])

lenlist = [math.inf] * (dot + 1)
def dfs(st, fin, cost):
    global lenlist
    if st == fin:
        print(cost)
        return
    lenlist[st] = cost
    for i in line[st]:
        newcost = cost + i[1]
        nextdot = i[0]
        if lenlist[nextdot] != math.inf:
            continue
        else:
            dfs(nextdot, fin, newcost)

for i in range(qu_num):
    fir, last = map(int, input().split())
    lenlist = [math.inf] * (dot + 1)
    dfs(fir, last, 0)