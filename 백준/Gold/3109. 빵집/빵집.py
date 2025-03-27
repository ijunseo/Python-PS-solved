#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input
n, m = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(n)]

#solve
ans = 0
wentlist = [[False] * m for _ in range(n)]

#dfs and greedy
def dfs(st):
    global ans
    global lst
    nowc, nowr = st
    lst[nowc][nowr] = 'x'
    if nowr == m - 1: #到達可能なら
        ans += 1
        return True #Trueをreturnする
    for i in range(3):
        nextc = nowc + next[i][0]
        nextr = nowr + next[i][1]
        if 0 <= nextc < n and 0 <= nextr < m and lst[nextc][nextr] != 'x' and not wentlist[nextc][nextr]: #範囲外、未探索、建物の存在を確認する
            if dfs([nextc, nextr]): 
                return True
            
#output
q = [[n - 1 - i, 0] for i in range(n)] #逆順で探索する
next = [[1, 1], [0, 1],[- 1, 1]] #右下、右、右上順で探索する
for i in q:
    dfs(i)
print(ans)