import sys 
input = sys.stdin.readline
import bisect

#input
n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

llst1 = [0] * n
llst2 = [0] * n
for i in range(n):
    now = lst1[i] - 1
    llst1[now] = i
    now = lst2[i] - 1
    llst2[now] = i

ans_lst_1 = []
ans_lst_2 = []

for i in range(n):
    now = lst1[i] - 1
    now_piv = llst2[now]

    if not ans_lst_1:
        ans_lst_1.append(now_piv)

    if now_piv < ans_lst_1[-1]:
        lft = bisect.bisect_left(ans_lst_1, now_piv)
        ans_lst_1[lft] = now_piv

    elif now_piv > ans_lst_1[-1]:
        ans_lst_1.append(now_piv)

print(len(ans_lst_1))