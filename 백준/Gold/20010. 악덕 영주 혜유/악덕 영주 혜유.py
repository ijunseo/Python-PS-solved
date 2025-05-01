#基本操作
import sys
input = sys.stdin.readline
import heapq
import math

#input 
n, m = map(int, input().split())
min_line = [[] for _ in range(n)]
for _ in range(m):
    st, ed, cst = map(int, input().split())
    min_line[st].append((cst, ed, st))
    min_line[ed].append((cst, st, ed))

min_went = [False] * (n)
min_went[0] = True
min_q = []
min_ans = 0
min_num = 0
for i in min_line[0]:
    heapq.heappush(min_q, i)

ans_line = [[] for _ in range(n)]
while min_q:
    if min_num == n:
        break
    next_cst, next_dot, now_dot = heapq.heappop(min_q)
    if min_went[next_dot]:
        continue
    min_went[next_dot] = True
    min_ans += next_cst
    ans_line[now_dot].append((next_cst, next_dot))
    ans_line[next_dot].append((next_cst, now_dot))
    for i in min_line[next_dot]:
        heapq.heappush(min_q, i)
print(min_ans)

def dik(st):
    went_lst = [math.inf] * n
    went_lst[st] = 0
    q = [(0, st)]

    while q:
        n_cst, n_dot = heapq.heappop(q)
        if went_lst[n_dot] < n_cst:
            continue
        went_lst[n_dot] = n_cst
        for i in ans_line[n_dot]:
            ne_cst = n_cst + i[0]
            ne_dot = i[1]
            if went_lst[ne_dot] > ne_cst:
                q.append((ne_cst, ne_dot))

    mx  = max(went_lst)
    for i in range(n):
        if went_lst[i] == mx:
            return i, mx
        
l, m = dik(0)
_, ans = dik(l)
print(ans)