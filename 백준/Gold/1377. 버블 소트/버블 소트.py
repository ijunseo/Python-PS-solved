#基本操作
import sys
input = sys.stdin.readline

#input 
n = int(input())
lst = []
for _ in range(n):
    now_num = int(input())
    lst.append(now_num)

dic = {}
sorted_lst = sorted(lst)

for i in range(n):
    now_ = sorted_lst[i]
    dic[now_] = i

ans = 0
for i in range(n):
    _now_num = lst[i]
    real_rank = dic[_now_num]
    if i > real_rank:
        ans = max(i - real_rank, ans)

print(ans + 1)