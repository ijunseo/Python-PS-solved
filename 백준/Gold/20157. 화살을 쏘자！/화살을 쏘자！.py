#基本操作
import sys
input = sys.stdin.readline
import bisect

#input 
n = int(input())
katamuki_1 = set()
katamuki_2 = set()
ka1 = []
ka2 = []
divpl = 0
divmin = 0
ans = 0
lft1 = 0
lft2 = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0:
        bisect.insort(ka1, y/x)
        katamuki_1.add(y/x)

    elif x < 0:
        bisect.insort(ka2, y/x)
        katamuki_2.add(y/x)

    else:
        if y > 0:
            divpl += 1
        else:
            divmin += 1

            
katamuki_1 = sorted(katamuki_1)
katamuki_2 = sorted(katamuki_2)
for i in katamuki_1:
    rgt1 = bisect.bisect_right(ka1, i)
    ans = max(ans, rgt1 - lft1)
    lft1 = rgt1

for i in katamuki_2:
    rgt2 = bisect.bisect_right(ka2, i)
    ans = max(ans, rgt2 - lft2)
    lft2 = rgt2

#output
print(max(ans,divpl, divmin))