import sys
input = sys.stdin.readline
import heapq
import math 


def findans(q):
  while q:
    if color[0] == 1:
      break
    nownum = heapq.heappop(q)
    nowcolor = color[nownum]
    for i in line[nownum]:
      if color[i] == 0:
        if nowcolor == color_1:
          color[i] = color_2
          heapq.heappush(q, i)
        elif nowcolor == color_2:
          color[i] = color_1
          heapq.heappush(q, i)
      else:
       if color[i] == nowcolor:
         color[0] = 1
       else:
         continue

dot, linenum = map(int, input().split())
color = [0] * (dot + 1)
line = [[] for _ in range(dot + 1)]
for i in range(linenum):
  a, b = map(int, input().split())
  line[a].append(b)
  line[b].append(a)
color_1 = 1
color_2 = 2
que = []
for i in range(1, dot + 1):
  if color[i] == 0:
    color[i] = color_1
    heapq.heappush(que, i)
    findans(que)
  #print(color)
if color[0] == 1:#隣の点の色が同じ時にcolor[0]を1にしたのでそれをスイッチとして使った。
  print('0')
else:
  print('1')