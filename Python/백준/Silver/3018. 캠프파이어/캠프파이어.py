#基本操作
import sys
input = sys.stdin.readline

#input 
n = int(input())
qnum = int(input())
lst = [[0] * (n + 1) for _ in range(qnum)]
for i in range(qnum):
	now = list(map(int, input().split()))
	now.pop(0)
	if 1 in now:
		for j in now:
			lst[i][j] = 1
	else:
		for j in range(1, n + 1):
			lst[i][j] = 1
		for j in range(i):
			for k in now:
				if lst[j][k] == 1:
					for k in now:
						lst[j][k] = 1
					break

#output

anslst = [True] * (n + 1)

for i in range(1, n + 1):
	for j in range(qnum):
		if lst[j][i] == 0:
			anslst[i] = False
			break
for i in range(1, n + 1):
	if anslst[i] == True:
		print(i)
			
			