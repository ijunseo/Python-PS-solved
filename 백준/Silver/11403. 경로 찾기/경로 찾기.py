import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
went = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    q = deque()
    q.append(i)
    check = [0 for _ in range(n)]

    while q:
        now = q.popleft()
        for j in range(n):
            if check[j] == 0 and lst[now][j] == 1:
                q.append(j)
                check[j] = 1
                went[i][j] = 1

for i in went:
    print(*i)
