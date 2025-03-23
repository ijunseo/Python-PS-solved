#基本操作
import sys
input = sys.stdin.readline
from collections import deque

#input
dot_num = int(input())
line =[[] for _ in range(dot_num + 1)]
line_num = int(input())
for _ in range(line_num):
    dot_1, dot_2 = map(int, input().split())
    line[dot_1].append(dot_2)
    line[dot_2].append(dot_1)
wentlist = [False] * (dot_num + 1)
ans = 0

#solve - bfs
q = deque([1])#パソコン1からウイルスが拡散する
while q:
    now = q.popleft()
    if not wentlist[now]:
        wentlist[now] = True
        ans += 1
        for i in line[now]:
            if not wentlist[i]:
                q.appendleft(i)
    else:
        continue

print(ans - 1) #1番パソコンはもう感染されているので

