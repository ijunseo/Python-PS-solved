import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 5)

'''
Tree_Dp問題
連続する点を選ばずに最大値を探して、また最大値が出るときの
点の集合をソートした順にPRINTする

Tree_dpとバックトラッキングを用いて解いた
'''

n = int(input())
lst = [0] + list(map(int, input().split()))
line = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    dot1, dot2 = map(int, input().split())
    line[dot1].append(dot2)
    line[dot2].append(dot1)

went = [False] * (n + 1)

#tree_dp
dp =  [[0, 0] for _ in range(n + 1)]
wentlst = [[[], []] for _ in range(n + 1)]
for i in range(1, n + 1):
    wentlst[i][1] += [i]
    dp[i][1] += lst[i]

def findtree(now_dot):
    global wentlst
    global went

    went[now_dot] = True
    for next in line[now_dot]:
        if went[next]:
            continue
        findtree(next)
        dp[now_dot][1] += dp[next][0]
        wentlst[now_dot][1] += wentlst[next][0]
        
        if dp[next][0] > dp[next][1]:
            dp[now_dot][0] += dp[next][0]
            wentlst[now_dot][0] += wentlst[next][0]

        else:
            dp[now_dot][0] += dp[next][1]
            wentlst[now_dot][0] += wentlst[next][1]


findtree(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    print(*sorted(wentlst[1][0]))
else:
    print(dp[1][1])
    print(*sorted(wentlst[1][1]))