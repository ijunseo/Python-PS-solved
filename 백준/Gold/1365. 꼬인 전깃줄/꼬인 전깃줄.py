#基本操作
import sys
input = sys.stdin.readline
import bisect

#input 
n = int(input())
lst_1 = list(map(int, input().split()))
for i in range(n):
    lst_1[i] -= 1

lst_2 = [0] * n
for i in range(n):
    now = lst_1[i]
    lst_2[n - 1 -  now] = n - 1 - i


sub_lst_1 = []
for i in range(n):
    now = lst_1[i]
    if not sub_lst_1:
        sub_lst_1.append(now)
    else:
        if now > sub_lst_1[-1]:
            sub_lst_1.append(now)
            continue
        else:
            rgt = bisect.bisect_right(sub_lst_1, now)
            sub_lst_1[rgt] = now

# sub_lst_2 = []
# for i in range(n):
#     now = lst_2[i]
#     if not sub_lst_2:
#         sub_lst_2.append(now)
#     else:
#         if now > sub_lst_2[-1]:
#             sub_lst_2.append(now)
#             continue
#         else:
#             rgt = bisect.bisect_right(sub_lst_2, now)
#             sub_lst_2[rgt] = now

# print(n - max(len(sub_lst_1), len(sub_lst_2)))
print(n - len(sub_lst_1))