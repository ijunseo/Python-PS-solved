import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
basis = []
for i in range(n):
    now = lst[i]
    for bas in basis:
        now = min(now ^ bas, now)
        if not now:
            break

    if now:
        basis.append(now)

ans = 0
for i in sorted(basis, reverse= True):
    ans = max(ans, ans ^ i)
print(ans)