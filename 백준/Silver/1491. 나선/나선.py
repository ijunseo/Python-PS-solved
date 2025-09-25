import sys
input = sys.stdin.readline


n, m = map(int, input().split())
k = min(n, m) // 2

if min(n, m) % 2 == 0:
    print(k - 1, k)
else:
    if n == m:
        print(k, k)
    elif n > m:
        print(n - 1 - k, k)
    else:
        print(k, m - 1 - k)