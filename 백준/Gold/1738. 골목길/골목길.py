#ベルマン–フォード法
import sys
import math
from copy import deepcopy
from collections import defaultdict
input = sys.stdin.readline

#ベルマン–フォード法
def bell():
    global pathdict
    global costlist
    for i in range(dot):
        for j in range(1, dot + 1):
            for k in line[j]:
                start = j
                dest, cost = k
                if costlist[start] != -math.inf and costlist[dest] < costlist[start] + cost:
                    costlist[dest] = costlist[start] + cost
                    pathdict[dest] = start#経路が更新されるたび、pathdictも更新する
                    if i == dot - 1:#負のサイクルが存在すると移動するcostをmath.inf（最大値）にする
                        costlist[dest] = math.inf
    return 
"""
dfsを用いて経路をlstに保存し、最後にlstをreuturn使用と考えたが、

def dfs(now, lst):
    newlst = deepcopy(lst)#経路を保存するリスト
    newlst.append(now)
    if now == dot:#目的地だと
        print(*newlst)#経路をプリント
        sys.exit()
    for i in line[now]:
        next, cost = i
        if costlist[next] == costlist[now] + cost:#理想的な最短経路だと（costlist）の最小値を維持すると
            dfs(next, newlst)#DFSを行う
"""
#データ入力
dot, linenum = map(int, input().split())
line = [[] for _ in range(dot + 1)]
pathdict = {}
costlist = [- math.inf] * (dot + 1)
costlist[1] = 0
for _ in range(linenum):
    st, ed, cst = map(int, input().split())
    line[st].append((ed, cst))
bell()
ans = []
pivot = dot
while pivot != 1:
    if costlist[pivot] == math.inf:
        print('-1')
        sys.exit()
    ans.append(pivot)
    pivot = pathdict[pivot]
ans.append(1)
print(*reversed(ans))