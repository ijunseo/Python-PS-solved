import sys
import heapq
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
dot, linenum = map(int, input().split())
def spanning(start):
  dotlist = [False] * (dot + 1)
  linelist = [[] for _ in range(dot + 1)]
  for _ in range(linenum):
    st, de, cst = map(int, input().split())
    linelist[st].append((de, cst))
    linelist[de].append((st, cst))
  dotlist[start] = True
  wentdot = 1
  que = []
  for i, j in linelist[start]:
    heapq.heappush(que, (j, i))
  ans = 0
  while wentdot < dot:
    cst, next = heapq.heappop(que)
    if dotlist[next] == True:
      continue
    dotlist[next] = True
    wentdot += 1
    ans += cst
    for i, j in linelist[next]:
      if dotlist[i] == False:
        heapq.heappush(que, (j, i))
  return ans
print(spanning(1))