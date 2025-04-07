#基本操作
import sys
input = sys.stdin.readline
import bisect

#input 
n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    lst[i] -= 1

sub_lst = []
for i in range(n):
    now = lst[i]
    if not sub_lst:
        sub_lst.append(now)
    else:
        if now > sub_lst[-1]:
            sub_lst.append(now)
            continue
        else:
            rgt = bisect.bisect_right(sub_lst, now)
            sub_lst[rgt] = now

print(n - len(sub_lst))