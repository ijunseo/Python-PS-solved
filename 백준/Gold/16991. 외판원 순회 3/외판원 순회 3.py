#基本操作
import sys
input = sys.stdin.readline
import math

#input 
n = int(input())
locate = []
for _ in range(n):
    nowlocate = list(map(int, input().split()))
    locate.append(nowlocate)



lst = [[0] * n for _ in range(n)]

def find_len(a, b):
    return (math.sqrt((locate[a][1] - locate[b][1]) ** 2 + (locate[a][0] - locate[b][0]) ** 2))
for i in range(n):
    for j in range(n):
        if not lst[i][j]:
            gap = find_len(i, j)
            lst[i][j] = gap 
            lst[j][i] = gap

dp_lst = [[math.inf] * n for _ in range(1 << n)]
dp_lst[0][0] = 0

#solve
for row in range(1 << n):
    for col in range(n):
        if dp_lst[row][col] == math.inf:
            continue

        for next in range(n):
            if next == 0:
                if row != (2 ** n - 2):
                    continue
            if not lst[col][next]:
                continue
            if next == col:
                continue
            else:
                next_piv = row | 1 << next
                if row != next_piv:
                    dp_lst[next_piv][next] = min(dp_lst[next_piv][next], dp_lst[row][col] + lst[col][next])

print(dp_lst[-1][0])