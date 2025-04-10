#基本操作
import sys
input = sys.stdin.readline
import bisect

#input 
n = int(input())
lst = list(map(int, input().split()))
llst = []
ans_lst = []
for i in range(n):
    now = lst[i]
    piv = bisect.bisect_left(llst, now)

    if not llst:
        llst.append(now)
    if piv > len(llst) - 1:
        llst.append(now)
        ans_lst.append(piv)
    else:
        llst[piv] = now
        ans_lst.append(piv)


lllst = []
ans = len(llst) - 1
print(ans + 1)
for i in range(n - 1, -1, -1):
    if ans_lst[i] == ans:
        lllst.append(lst[i])
        ans -= 1
for i in reversed(lllst):
    print(i, end = ' ')