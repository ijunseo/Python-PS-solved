import sys
input = sys.stdin.readline
dot = int(input())
line =[[] for _ in range(dot + 1)]
for i in range(dot - 2):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)
wentlist = [False] * (dot + 1)
wentlist[1] = True
from collections import deque
def find(a):
  que = deque()
  que.append(a)
  while que:
    now = que.popleft()
    for i in line[now]:
      if not wentlist[i]:
        wentlist[i] = True
        que.append(i)
find(1)
for i in range(1, dot + 1):
    if not wentlist[i]:
        print(1, i)
        break