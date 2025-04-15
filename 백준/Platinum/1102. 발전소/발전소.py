#基本操作
import sys
input = sys.stdin.readline
import math

#input 
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp_lst = [-1 for _ in range(1 << n)]

st = input().rstrip()

now_piv = 0
ll = len(st)
checklst = []
ans_check = int(input())

#YNN -> 4, YYNN -> 12 NYN -> 2
for i in range(ll - 1, -1, -1):
    if st[i] == 'Y':
        checklst.append(i)
        now_piv += 2 ** (i)

#solve 
for i in checklst:
    dp_lst[now_piv] = 0

for i in range(1 << n):
    if dp_lst[i] == -1:
        continue

    now_one_lst = set()
    first_check = bin(i)[2:]

    for piv in range(len(first_check)):
        if first_check[- 1 - piv] == '1':
            now_one_lst.add(piv)

    for next in range(n):
        if next in now_one_lst:
            continue

        for now_piv in now_one_lst:
            nextpiv = i | (1 << next)
            if i == nextpiv:
                continue

            if dp_lst[nextpiv] == -1:
                dp_lst[nextpiv] = dp_lst[i] + lst[now_piv][next]

            else:
                dp_lst[nextpiv] = min(dp_lst[nextpiv], dp_lst[i] + lst[now_piv][next])

ans = math.inf
for i in range(1 << n):
    if bin(i)[2:].count('1') == ans_check:
        if dp_lst[i] == -1:
            continue
        if dp_lst[i] < ans:
            ans = dp_lst[i]

if ans_check <= len(checklst):
    print('0')
    sys.exit()

print('-1' if ans == math.inf else ans)