import sys
input = sys.stdin.readline
import math
dot = int(input())

dplist = [[math.inf] * (dot + 1) for _ in range(dot + 1)]
for i in range(1, dot + 1):
    dplist[i][i] = 0
while True:
    a, b = map(int, input().split())
    if a == -1 and  b == -1:
        break
    dplist[a][b] = 1
    dplist[b][a] = 1

for k in range(1, dot + 1):
    for i in range(1, dot + 1):
        for j in range(1, dot + 1):
            dplist[i][j] = min(dplist[i][j], dplist[i][k] + dplist[k][j])


#print(dplist)
anslist = []
now = math.inf
for i in range(1, dot + 1):
    nowlist = dplist[i]
    nowmax = 0
    for j in range(1, dot + 1):
        if nowlist[j] == math.inf:
            continue
        else:
            nowmax = max(nowmax, nowlist[j])
    now = min(nowmax, now)
    anslist.append([nowmax, i])
ans = []
for i in range(dot):
    if anslist[i][0] == now:
        ans.append(anslist[i][1])
#print(anslist)
member = len(ans)
print(now , member)
ans.sort()
print(*ans)
#print(now)