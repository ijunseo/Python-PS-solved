import sys
input = sys.stdin.readline
import bisect

#Input
tc = int(input())

for _ in range(tc):
    n1, n2 = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    llst = sorted((map(int, input().split())))
    ans = 0
    for i in range(n1):
        now = lst[i]
        lft = bisect.bisect_left(llst, now)
        ans += lft
    print(ans)
