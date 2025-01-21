#基本操作
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)#全ての点が繋がってるならdfsのrecursionが10^5になるので

#アルゴリズム
def dfs(now, start_piv):
    global piv
    global ans
    global wentlist
    wentlist[now] = piv
    piv += 1
    if wentlist[numlist[now]] >= start_piv:
    #次に行く点が今のサイクルに属してるなら
        ans += piv - wentlist[numlist[now]]#ansにサイクルの大きさを足す
        return
    elif wentlist[numlist[now]] == 0:
    	dfs(numlist[now], start_piv)
    else:
    	return

#入力
testcase = int(input())
for _ in range(testcase):
    num = int(input())#数字の数
    numlist = [0] + list(map(int, input().split()))#入力されるlist
    wentlist = [0] * (num + 1)
    piv = 1
    ans = 0
    for i in range(1, num + 1):
        if wentlist[i] == 0:
        	dfs(i, piv)
    print(num - ans)
