import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	a = float(input())
	lst.append(a)
lst.sort()

for i in range(7):
	print('{:.3f}'.format(lst[i]))
	