#基本操作
import sys
import math
input = sys.stdin.readline

#input
num, start = map(int, input().split())
lst = [list(map(int, input().split()))for _ in range(num)]

#訪問check
went = [False] * num
went[start] = True

#solve - floyd - warshall
for j in range(num):
    for i in range(num):
        for k in range(num):
            if lst[i][k] > lst[i][j] + lst[j][k]:
                lst[i][k] = lst[i][j] + lst[j][k]

ans = math.inf
#solve - backtracking
def findans(now, cst, wentnum):
    global ans
    if wentnum == num:
        ans = min(ans, cst)
        return
    for i in range(num):
        if not went[i]:#まだ未訪問
            went[i] = True
            findans(i, cst + lst[now][i], wentnum + 1)
            went[i] = False#戻す

#output
findans(start, 0, 1)
print(ans)