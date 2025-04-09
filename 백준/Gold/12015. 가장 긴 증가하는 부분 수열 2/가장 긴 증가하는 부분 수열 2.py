#基本操作
import sys
input = sys.stdin.readline
import bisect

#input 
n = int(input())
lst = list(map(int, input().split()))
ans_lst = []
for i in range(n):
    now = lst[i]
    if not ans_lst:
        ans_lst.append(now)
        
    if now < ans_lst[-1]:
        lft = bisect.bisect_left(ans_lst, now)
        ans_lst[lft] = now
    elif now > ans_lst[-1]:
        ans_lst.append(now)

print(len(ans_lst))