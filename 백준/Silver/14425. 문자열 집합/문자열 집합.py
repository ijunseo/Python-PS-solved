import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
ans = 0

for _ in range(n):
    inp = str(input().rstrip())
    s.add(inp)
for _ in range(m):
    inp = str(input().rstrip())
    if inp in s:
        ans += 1
print(ans)