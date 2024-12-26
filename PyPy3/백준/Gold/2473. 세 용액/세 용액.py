import sys
input = sys.stdin.readline
num = int(input())
numlist = list(map(int, input().split()))
numlist.sort()
import math
minabs = math.inf
ans = []
#print(numlist)
def findmin(now, lst):
    global minabs
    global ans
    length = len(lst)
    lft = 0
    rgt = length - 1
    if length < 2:
        return
    while True:
        if lft == rgt:
            return
        lftnum = lst[lft]
        rgtnum = lst[rgt]
        nowans = now + lftnum + rgtnum
        if abs(nowans) < minabs:
            minabs = abs(nowans)
            ans = [now, lftnum, rgtnum]
        if nowans < 0:
            lft += 1
        elif nowans == 0:
            print(*ans)
            sys.exit()
        elif nowans > 0:
            rgt -= 1


for i in range(num - 2):
    nownum = numlist[i]
    newlist = numlist[i + 1:]
    #print(nownum, newlist)
    findmin(nownum, newlist)
print(*ans)