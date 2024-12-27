import sys
input = sys.stdin.readline
singer, staff = map(int, input().split())
line = [[]for _ in range(singer + 1)]
linenumlist = [0] * (singer + 1)

for i in range(staff):
    cmd = list(map(int, input().split()))
    num = cmd[0]
    for j in range(num - 1):
        line[cmd[j + 1]].append(cmd[j + 2])
        linenumlist[cmd[j + 2]] += 1
from collections import deque
que = deque()
ans = []
for i in range(1, singer + 1):
    if linenumlist[i] == 0:
        que.append(i)
while que:
    now = que.popleft()
    ans.append(now)
    for i in line[now]:
        linenumlist[i] -= 1
        if linenumlist[i] == 0:
            que.append(i)
for i in range(1, singer + 1):
	if linenumlist[i] != 0:
		print('0')
		sys.exit()
for i in ans:
	print(i)