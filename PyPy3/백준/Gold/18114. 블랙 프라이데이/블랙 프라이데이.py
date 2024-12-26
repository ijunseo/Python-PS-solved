import sys
input = sys.stdin.readline
import bisect
num, target = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()
ans = 0
ans += bisect.bisect_right(numlist, target) - bisect.bisect_left(numlist, target)
if ans > 0:
  print('1')
  sys.exit()
start = 0
end = num - 1
while start < end:
  if numlist[start] + numlist[end] > target:
    end -= 1
  elif numlist[start] + numlist[end] < target:
    start += 1
  else:
    print('1')
    sys.exit()
    #ans += 1
    #start += 1

def findmin(now, lst):
    #global ans
    length = len(lst)
    lft = 0
    rgt = length - 1
    if length < 2:
        return
    while lft < rgt:
        lftnum = lst[lft]
        rgtnum = lst[rgt]
        nowans = now + lftnum + rgtnum
        if nowans < target:
            lft += 1
        elif nowans == target:
            print('1')
            sys.exit()
            #ans += 1
            #lft += 1
        elif nowans > target:
            rgt -= 1


for i in range(num - 2):
    nownum = numlist[i]
    newlist = numlist[i + 1:]
    findmin(nownum, newlist)
print('0')