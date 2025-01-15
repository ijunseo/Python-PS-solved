#基本操作
import sys
import math
input = sys.stdin.readline

#入力
length, target = map(int , input().split())
if target == 0:#例外
	print('1')
	sys.exit()
qlist = list(map(int,input().split()))
sumlist = [0]
now = 0
for i in range(length):
	now += qlist[i]
	sumlist.append(now)

#twopointer
lft = 0
rgt = 0
ans = math.inf

while True:
	nowsum = sumlist[rgt] - sumlist[lft]
	if nowsum < target:
		if rgt == length:
			break
		rgt += 1 
	if nowsum >= target:
		ans = min(ans, rgt - lft)
		if rgt == lft + 1:
			break
		lft += 1
print('0' if ans == math.inf else ans)