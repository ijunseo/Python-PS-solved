st = str(input().rstrip())
n = len(st)

for i in range(n):
    now = st[i:]
    if now == now[::-1]:
        print(2 * n - len(now))
        break