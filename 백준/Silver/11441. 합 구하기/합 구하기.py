import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

lllst = [0]
for i in range(n):
    lllst.append(lllst[-1] + lst[i])

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(lllst[r] - lllst[l - 1])
