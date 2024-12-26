import sys
input = sys.stdin.readline
num = input().split("-")
anslist = []
for i in num:
    ans = 0
    ex = i.split("+")
    for j in ex:
        ans += int(j)
    anslist.append(ans)
a = -sum(anslist)
a += anslist[0] * 2
print(a)
