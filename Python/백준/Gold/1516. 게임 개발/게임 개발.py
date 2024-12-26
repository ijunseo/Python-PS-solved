import sys
input = sys.stdin.readline
dot = int(input())
linelist = [[]for _ in range(dot + 1)]
buildtime = [0] * (dot + 1)
linenumlist = [0] * (dot + 1)
anstime = [0] * (dot + 1)
for i in range(dot):
    cmd = list(map(int, input().split()))
    buildtime[i + 1] = cmd[0]
    for j in cmd[1:]:
        if j == -1:
            break
        linelist[j].append(i + 1)
        linenumlist[i + 1] += 1
from collections import deque
que = deque()
for i in range(1, dot + 1):
    if linenumlist[i] == 0:
        que.append(i)
while que:
    now = que.popleft()
    for i in linelist[now]:
        anstime[i] = max(anstime[i], anstime[now] + buildtime[now])
        linenumlist[i] -= 1
        if linenumlist[i] == 0:
            que.append(i)
for i in range(1, dot + 1):
	print(anstime[i] + buildtime[i])