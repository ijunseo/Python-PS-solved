import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    q.append(list(map(int, input().split())))

q.sort(key = lambda x : x[0], reverse = True)
ans_lst = []
ans_num = 0
while q:
    now_dead, now_cup = q.pop()
    heapq.heappush(ans_lst, now_cup)
    ans_num += 1

    if ans_num > now_dead:
        ans_num -= 1
        heapq.heappop(ans_lst)

print(sum(ans_lst))