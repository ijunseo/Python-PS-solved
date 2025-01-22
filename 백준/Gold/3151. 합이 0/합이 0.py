#基本操作
import sys
input = sys.stdin.readline
import bisect

#入力
num = int(input())
numlist = sorted(list(map(int, input().split())))

#solve
ans = 0
for i in range(num - 2):
    lft = i + 1
    rgt = num - 1
    while lft < rgt:
        nownum = numlist[i] + numlist[lft] + numlist[rgt]
        if nownum < 0:
            lft += 1
        if nownum > 0:
            rgt -= 1
        if nownum == 0:
            if numlist[lft] == numlist[rgt]:
                ans += rgt - lft
            else:
                piv = bisect.bisect_left(numlist, numlist[rgt])
                ans += rgt - piv + 1
            lft += 1
print(ans)
