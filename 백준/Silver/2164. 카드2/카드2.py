import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque([i for i in range(n, 0, -1)])
while q:
    now = q.pop()
    if not q:
        print(now)
        sys.exit()
    else:
        now = q.pop()
        q.appendleft(now)