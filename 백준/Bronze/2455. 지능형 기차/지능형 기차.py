import sys
input = sys.stdin.readline

mx = 0
n = 0
for _ in range(4):
    a, b = map(int, input().split())
    n += b - a
    mx = max(mx, n)
print(mx)