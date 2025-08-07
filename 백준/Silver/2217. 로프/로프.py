import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
mx  =0
for i in range(n):
    mx = max(mx, lst[i] * (n - i))
print(mx)