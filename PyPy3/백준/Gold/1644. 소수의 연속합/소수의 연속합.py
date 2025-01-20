#基本操作
import sys
input = sys.stdin.readline
import math

#入力
target = int(input())

#素数判定(エラトステネスの篩)
numlst = [True for i in range(4_000_001)]
mxsqrt = int(math.sqrt(4_000_001) + 1)
for i in range(2, mxsqrt):
	if numlst[i] == True:
		piv = 2
		while i * piv < 4_000_001:
			numlst[i * piv] = False
			piv += 1
primelst = [0]
for i in range(2, 4_000_001):#0, 1は素数ではないので
	if numlst[i] == True:
		primelst.append(i)

#twopointer
lft = 0 #left pivot
rgt = 1 #right pivot
now = 2 #累積合
ans = 0 #今まで何回target == nowだったのか
while True:
	if now == target:
		ans += 1 
		if rgt == len(primelst) - 1:
			break
		rgt += 1 
		if primelst[rgt] > target:
			break
		now += primelst[rgt]
	elif now < target:
		if rgt == len(primelst) - 1:
			break
		rgt += 1 
		if primelst[rgt] > target:
			break
		now += primelst[rgt]
	elif now > target:
		now -= primelst[lft]
		lft += 1 
print(ans)