import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    a, b =map(int, input().split())
    lst.append((a, b))

for i in range(n):
    nowx, nowy = lst[i]
    rank = 1
    for j in range(n):
        if i == j:
            continue
        nx, ny = lst[j]
        if nowx < nx and nowy < ny:
            rank += 1
    print(rank, end =' ')