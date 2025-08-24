import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int,input().split()))

lst.sort()
l, r = 0, len(lst) - 1
ans = 0

while l < r:
    s = lst[l] + lst[r]
    if s < m:
        l += 1
    elif s > m:
        r -= 1
    else:
        ans += 1
        l += 1
        r -= 1
print(ans)