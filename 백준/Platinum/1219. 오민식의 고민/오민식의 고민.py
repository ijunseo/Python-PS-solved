import sys
import math
input = sys.stdin.readline

#入力
num, start, destination, linenum = map(int, input().split())
line = [[] for _ in range(num)]
for i in range(linenum):
    st, de, cst = map(int, input().split())
    line[st].append((de, cst))
cost = list(map(int, input().split()))
costlist = [- math.inf] * num
costlist[start] = cost[start]

#ベルマン–フォード法
for i in range(num):
    for j in range(num):
        for k in line[j]:
            start = j
            next, cst = k
            if costlist[j] != - math.inf and costlist[next] < costlist[j] - cst + cost[next]:
                costlist[next] = costlist[j] - cst + cost[next]
                if i == num - 1:
                    costlist[next] = math.inf

#二重サイクルcheck用のDFS
def dfs(now):
    global costlist
    for i in line[now]:
        if costlist[i[0]] == math.inf:
            continue
        costlist[i[0]] = math.inf
        dfs(i[0])
    return
"""
3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000
のように同じ点で繰り返すと、costlist[1] = math.inf, costlist[2] = 20000になる問題が生じたので、
DFS関数でmath.infから行ける点のcostlist値をmath.infにした。
"""

#答え
check = set()
for i in range(num):
    if costlist[i] == math.inf:
        dfs(i)

if costlist[destination] == math.inf:
    print('Gee')
elif costlist[destination] == - math.inf:
    print('gg')
else:
    print(costlist[destination])