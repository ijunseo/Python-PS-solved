import math
import sys

input = sys.stdin.readline
num = int(input())
numlist = list(map(int, input().split()))
minabs = math.inf
ans = []
start, end = 0, num - 1
try:
	while True:
		if start == end:
			break
		nowgap = numlist[start] + numlist[end]
		if nowgap == 0:
			ans = [start, end]
			break
		if abs(nowgap) < minabs:
			ans = [start, end]
			minabs = abs(nowgap)
			#print(ans)
			#print(minabs)
		if nowgap < 0:
			start += 1
		elif nowgap > 0:
			end -= 1
	for i in ans:
		print(numlist[i], end = ' ')
except:
	for i in ans:
		print(numlist[i], end = ' ')
