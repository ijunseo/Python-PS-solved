#基本操作
import sys
input = sys.stdin.readline

#input 
num, qnum = map(int, input().split())
lst = [[0] * (num + 1)]
for _ in range(num):
	nowlst = [0] + list(map(int, input().split()))
	lst.append(nowlst)
	
#Floyd-Warshall
for j in range(1, num + 1):
	for i in range(1, num + 1):
		for k in range(1, num + 1):
			if lst[i][k] > lst[i][j] + lst[j][k]:
				lst[i][k] = lst[i][j] + lst[j][k]
				
#output
for _ in range(qnum):
	st, ed, cst = map(int, input().split())
	if lst[st][ed] > cst:
		print('Stay here')
	else:
		print('Enjoy other party')