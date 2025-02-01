#基本操作
import sys
input = sys.stdin.readline

#input 
n = int(input())
katamuki_1 = set()
katamuki_2 = set()
ka1 = {}
ka2 = {}
divpl = 0
divmin = 0
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0:
        now = y/x
        if now in katamuki_1:
            ka1[now] += 1
        else:
            katamuki_1.add(now)
            ka1[now] = 1

    elif x < 0:
        now = y/x
        if now in katamuki_2:
            ka2[now] += 1
        else:
            katamuki_2.add(now)
            ka2[now] = 1

    else:
        if y > 0:
            divpl += 1
        else:
            divmin += 1

for i in katamuki_1:
    ans = max(ans, ka1[i])


for i in katamuki_2:
    ans = max(ans, ka2[i])

#output
print(max(ans, divpl, divmin))