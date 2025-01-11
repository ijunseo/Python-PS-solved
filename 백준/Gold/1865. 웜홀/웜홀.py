#ベルマン–フォード法
import sys
import math

input = sys.stdin.readline
testcase = int(input())

#ベルマン–フォード法
def bell():
    #costlist = [math.inf] * (dot + 1)はmath.inf互いの大小関係を確認できないため、エラーが発生
    costlist = [10000] * (dot + 1)
    for i in range(dot):
        for j in range(len(line)): #両方向グラフなのでlinenum * 2
            start, dest, cost = line[j]
            if costlist[dest] >  costlist[start] + cost:
                costlist[dest] = costlist[start] + cost
                if i == dot - 1:
                    return print('YES')
    return print('NO')

for _ in range(testcase):
    #データ入力
    dot, linenum, wormholenum = map(int, input().split())
    line = []
    for _ in range(linenum):
        st, ed, cst = map(int, input().split())
        line.append((st, ed, cst))
        line.append((ed, st, cst))
    for _ in range(wormholenum):
        st, ed, cst = map(int, input().split())
        line.append((st, ed, -cst))
    bell()