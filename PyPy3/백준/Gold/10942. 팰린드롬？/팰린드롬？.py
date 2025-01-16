#基本操作
import sys
input = sys.stdin.readline

#入力
num = int(input())
numlist = list(map(int, input().split()))
qnum = int(input())

#is palindrome?
dplist = [[0] * num for _ in range(num)]
for j in range(num):
	for i in range(j + 1):
		if i == j:
			dplist[i][j] = 1#palindrome
		elif numlist[i] == numlist[j]:
			if j - 1 == i:
				dplist[i][j] = 1
			elif dplist[i + 1][j - 1] == 1:
				dplist[i][j] = 1


for _ in range(qnum):
	st, ed = map(int, input().split())
	print(dplist[st - 1][ed - 1])