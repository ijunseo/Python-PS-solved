#基本操作
import sys
input = sys.stdin.readline

#input 
ans = 0
n = int(input())
lst = []
for _ in range(n):
    now_str = str(input().rstrip())
    len_str = len(now_str)
    ans = max(ans, len_str)
    lst.append([len_str, now_str[0], now_str[-1]])

llst = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if lst[i][2] == lst[j][1]:
                llst[i][j] = lst[j][0]

dp_lst = [[-1] * n for _ in range(1 << n)]

for i in range(n):
    dp_lst[1 << i][i] = lst[i][0]

#solve
for row in range(1 << n):
    for col in range(n):
        if dp_lst[row][col] == -1:
            continue

        for next in range(n):
            if not llst[col][next]:
                continue
            if next == col:
                continue
            else:
                next_piv = row | 1 << next
                if row != next_piv:
                    dp_lst[next_piv][next] = max(dp_lst[next_piv][next], dp_lst[row][col] + llst[col][next])
                    ans = max(ans, dp_lst[next_piv][next])

print(ans)