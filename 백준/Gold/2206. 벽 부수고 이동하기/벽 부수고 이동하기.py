import sys
import math
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())

numlist = [['1'] * (col + 1)]
for _ in range(row):
    imsilist = ['1'] + list(input().strip())
    numlist.append(imsilist)

ans_lst = [[[math.inf, math.inf] for _ in range(col + 1)] for _ in range(row + 1)]
ans_lst[1][1][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque([(1, 1)])

while q:
    now_r, now_c = q.popleft()
    zero_cost, one_cost = ans_lst[now_r][now_c][0], ans_lst[now_r][now_c][1]

    for i in range(4):
        next_r = now_r + dx[i]
        next_c = now_c + dy[i]
        if not 1 <= next_r <= row or not 1 <= next_c <= col:
            continue 

        if numlist[next_r][next_c] == '0':
            if ans_lst[next_r][next_c][0] > zero_cost + 1:
                ans_lst[next_r][next_c][0] = zero_cost + 1
                q.append((next_r, next_c))
            if ans_lst[next_r][next_c][1] > one_cost + 1:
                ans_lst[next_r][next_c][1] = one_cost + 1
                q.append((next_r, next_c))
        elif numlist[next_r][next_c] == '1':
            if ans_lst[next_r][next_c][1] > zero_cost + 1:
                ans_lst[next_r][next_c][1] = zero_cost + 1
                q.append((next_r, next_c))

ans = ans_lst[row][col]
print('-1' if ans[0] == math.inf and ans[1] == math.inf else min(ans))