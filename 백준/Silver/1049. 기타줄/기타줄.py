n, m = map(int, input().split())

A = []
B = []
for _ in range(m):
    x, y = map(int, input().split())
    A.append(x)
    B.append(y)

a = min(A)
b = min(B)

ans = min(n//6 * a + n % 6 * b, (n // 6 + 1) * a, n * b)
print(ans)
