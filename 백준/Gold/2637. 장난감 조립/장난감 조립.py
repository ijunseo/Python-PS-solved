import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dot = int(input())
linenum = int(input())

line = [[] for _ in range(dot + 1)]
isparlist = [False] * (dot + 1)
indeg = [0] * (dot + 1)

for _ in range(linenum):
    a, b, c = map(int, input().split())
    isparlist[a] = True
    line[b].append((a, c))
    indeg[a] += 1

ansset = set()
anslist = [0] * (dot + 1)
for i in range(1, dot + 1):
    if not isparlist[i]:
        ansset.add(i)

need = [defaultdict(int) for _ in range(dot + 1)]
q = deque()
for i in range(1, dot + 1):
    if indeg[i] == 0:
        need[i][i] = 1
        q.append(i)

while q:
    now = q.popleft()
    for nxt, cnt in line[now]:
        for k, v in need[now].items():
            need[nxt][k] += v * cnt
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            q.append(nxt)

for i in ansset:
    anslist[i] = need[dot][i]

for i in range(1, dot + 1):
    if anslist[i]:
        print(i, anslist[i])