import sys
input = sys.stdin.readline
import math
dot, lnum = map(int, input().split())
line = [[] for i in range(dot + 1)] 
for i in range(lnum):
  a, b = map(int, input().split())
  line[a].append(b)
  line[b].append(a)

dotlist = [0 for i in range(dot + 1)]
dotlist[0] = 1

def find(st):
  global dotlist
  for i in line[st]:
    if dotlist[i] == 0:
      dotlist[i] = 1
      find(i)
    elif dotlist[i] == 1:
      continue
ans = 0
for i in range(dot + 1):
  if dotlist[i] == 0:
    find(i)
    ans += 1
  elif dotlist[i] == 1:
    continue
print(ans)
  