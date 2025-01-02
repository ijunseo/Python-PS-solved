import sys
input = sys.stdin.readline
dot, linenum = map(int, input().split())
line = [[] for _ in range(dot + 1)]
linenumlist = [0] * (dot + 1)
anslist = [0] * (dot + 1)

for _ in range(linenum):
    a, b = map(int, input().split())
    line[a].append(b)
    linenumlist[b] += 1
from collections import deque
que = deque()

for i in range(1, dot + 1):
    if linenumlist[i] == 0:
        anslist[i] += 1
        que.append(i)

while que:
    now = que.popleft()
    for i in line[now]:
        linenumlist[i] -= 1
        if linenumlist[i] == 0:
            anslist[i] = anslist[now] + 1
            que.append(i)
print(*anslist[1:])