#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input 
n, l = map(int, input().split())

q = list(map(int, input().split()))

ans_q = deque([])

for i in range(n):
    while ans_q:
        if ans_q[-1][0] > q[i]:
            ans_q.pop()
        else:
            break

    while ans_q:
        if ans_q[0][1] < i - l + 1:
            ans_q.popleft()
        else:
            break

    ans_q.append([q[i],i])
    print(ans_q[0][0], end = ' ')