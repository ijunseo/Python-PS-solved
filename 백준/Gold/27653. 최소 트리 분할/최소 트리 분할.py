#基本操作
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5 + 1)

#input 
n = int(input())
lst = list(map(int, input().split()))
line = [[] for _ in range(n)]

for i in range(n - 1):
    dot1, dot2 = map(int, input().split())
    line[dot1 - 1].append(dot2 - 1)
    line[dot2 - 1].append(dot1 - 1)

ans = 0
wentlist = [0] * n

#bfs
def bfs(nowdot, nowcost):
    global ans
    global wentlist
    if wentlist[nowdot]:
        return
    
    wentlist[nowdot] = 1
    if lst[nowdot] >= nowcost:
        ans += lst[nowdot] - nowcost
        for i in line[nowdot]:
            bfs(i, lst[nowdot])
    
    else:
        for i in line[nowdot]:
            bfs(i, lst[nowdot])

ans += lst[0]
bfs(0, lst[0])
print(ans)