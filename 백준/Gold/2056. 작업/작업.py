import sys
input = sys.stdin.readline
dot = int(input())
buildlist = [0] * (dot +1)
timelist = [0] *(dot + 1)
line = [[] for _ in range(dot + 1)]
linenumlist = [0] *(dot + 1)
for i in range(dot):
    now = list(map(int,input().split()))
    buildlist[i + 1] = now[0]
    dotnum = now[1]
    for j in range(dotnum):
        num = now[2+j]
        line[num].append(i + 1)
        linenumlist[i + 1]+=1
from collections import deque
que = deque()
for i in range(1,dot +1):
    if linenumlist[i]== 0:
        que.append(i)
while que:
    now = que.popleft()
    timelist[now]+=buildlist[now]
    for i in line[now]:
        timelist[i]=max(timelist[i], timelist[now])
        linenumlist[i]-=1
        if linenumlist[i]==0:
            que.append(i)
print(max(timelist))