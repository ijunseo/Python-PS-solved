#基本操作
import sys
input = sys.stdin.readline

#input
n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
now = lst[0]
anslist = [-1] * n 
for i in range(n):
    if now != lst[i]:
        now = lst[i]
        anslist[i] = i
    else:
        anslist[i] = anslist[i - 1]
anslist.reverse()
piv = n + 1

#output
for i in range(n):
    if anslist[i] == -1:
        print('-1', end = ' ')
    else:
        print(piv - anslist[i], end = ' ')