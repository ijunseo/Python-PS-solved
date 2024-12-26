import sys
input = sys.stdin.readline
dot, linenum = map(int, input().split())
line = [[] for _ in range(dot + 1)]
for _ in range(linenum):
    st, de, cst = map(int, input().split())
    line[st].append((de, cst))
    line[de].append((st, cst))
dotlist = [False] * (dot + 1)
ans = []
from heapq import *
que = [(0, 1)]
while que:
    nowcst, nowdot = heappop(que)
    if dotlist[nowdot]:
        continue
    ans.append(nowcst)
    dotlist[nowdot] = True
    for next, cst  in line[nowdot]:
        heappush(que, (cst, next))
print(sum(ans) - max(ans))