#基本操作
import sys
input = sys.stdin.readline

#input
a, b, c = map(int, input().split())
setnum = min(a, b, c)
bugger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))
bugger.sort(reverse = True)
side.sort(reverse = True)
drink.sort(reverse = True)

#output
ans1 = sum(bugger) + sum(side) + sum(drink)
setmoney = 0
for i in range(setnum):
	setmoney += bugger[i] + side[i] + drink[i]
ans2 = int(ans1 - setmoney * 0.1) 
print(ans1)
print(ans2)