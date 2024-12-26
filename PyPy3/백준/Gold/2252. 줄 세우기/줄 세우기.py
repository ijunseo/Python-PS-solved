import sys
input = sys.stdin.readline
dot, line = map(int,input().split())
dotlist = [[] for _ in range(dot + 1)]
findstartdot = [0] * (dot + 1)
from collections import deque
ans = []
que = deque()

for _ in range(line):
    a, b = map(int, input().split())
    dotlist[b].append(a)
    findstartdot[a] += 1

for i in range(1, dot + 1):
    if findstartdot[i] == 0:
        que.append(i)
while que:
    now = que.popleft()
    ans.append(now)
    for i in dotlist[now]:
        findstartdot[i] -= 1
        if findstartdot[i] == 0:
            que.append(i)

print(*reversed(ans))