#基本操作
import sys
input = sys.stdin.readline

#input
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

st = 0.5
ans = 0
for i in range(n):
    now = lst[i]
    if now > st:
        st = now - 0.5
        ans += 1
        st += m
    else:
        continue
print(ans)