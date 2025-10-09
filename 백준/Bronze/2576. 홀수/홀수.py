import sys
input = sys.stdin.readline

lst = []
for _ in range(7):
    lst.append(int(input()))

ans = 0
ans1 = 1000000

for i in range(7):
    now = lst[i]
    if now % 2:
        ans += now
        ans1 = min(ans1, now)

if not ans:
    print(-1)
    exit()
print(ans)
print(ans1)

