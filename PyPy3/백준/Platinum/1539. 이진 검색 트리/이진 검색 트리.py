import sys
input = sys.stdin.readline
dot = int(input())
dotlist = [[None, None, None] for _ in range(dot)]
root = int(input())
dotlist[root][2] = 1
import bisect
dotset = []
bisect.insort(dotset, root)
def find(nownum):
  lft = bisect.bisect_left(dotset, nownum)
  if lft == 0:
    bigdot = dotset[0]
    dotlist[bigdot][0] = nownum
    dotlist[nownum][2] = dotlist[bigdot][2] + 1
    bisect.insort(dotset, nownum)
    return
  elif lft == len(dotset):
    smalldot = dotset[-1]
    dotlist[smalldot][1] = nownum
    dotlist[nownum][2] = dotlist[smalldot][2] + 1
    bisect.insort(dotset, nownum)
    return
  else:
    bigdot = dotset[lft]
    smalldot = dotset[lft - 1]
    if dotlist[bigdot][2] > dotlist[smalldot][2]:
      dotlist[bigdot][0] = nownum
      dotlist[nownum][2] = dotlist[bigdot][2] + 1
      bisect.insort(dotset, nownum)
    else:
      dotlist[smalldot][1] = nownum
      dotlist[nownum][2] = dotlist[smalldot][2] + 1
      bisect.insort(dotset, nownum)
  return
for _ in range(dot - 1):
  num = int(input())
  find(num)
ans = 0
for i in dotlist:
	ans += i[2]
print(ans)