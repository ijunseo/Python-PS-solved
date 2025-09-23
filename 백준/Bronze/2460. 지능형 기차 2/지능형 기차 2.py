a = 0
b = 0

for _ in range(10):
    out, come = map(int, input().split())
    a += come - out
    b = max(a, b)

print(b)