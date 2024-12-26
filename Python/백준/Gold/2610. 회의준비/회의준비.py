import sys
input = sys.stdin.readline
dot = int(input())
linenum = int(input())
import math
line = [[math.inf] * (dot + 1)for _ in range(dot + 1)]
for _ in range(linenum):
  a, b= map(int, input().split())
  line[a][b] = 1
  line[b][a] = 1
for j in range(1, dot + 1):
  for i in range(1, dot + 1):
    for k in range(1, dot + 1):
      if line[i][k] > line[i][j] + line[j][k]:
        line[i][k] = line[i][j] + line[j][k]
for i in range(1, dot + 1):
	line[i][i] = math.inf
findlist = [False] * (dot + 1)
def findans(dotnum):
  global findlist
  maxnum = math.inf
  ans = False
  que = []
  lst = line[dotnum]
  for i in range(1, dot + 1):
    if lst[i] != math.inf:
      que.append(i)
      findlist[i] = True
  for i in que:
    nowquemax = 0
    for j in line[i]:
      if j == math.inf:
        continue
      nowquemax = max(nowquemax, j)
    if nowquemax < maxnum:
      maxnum = nowquemax
      ans = i
  if ans == False:
    return dotnum
  return ans
anslist = []
for i in range(1, dot + 1):
  if findlist[i] == False:
    anslist.append(findans(i))
anslist.sort()
print(len(anslist))
for i in anslist:
  print(i)