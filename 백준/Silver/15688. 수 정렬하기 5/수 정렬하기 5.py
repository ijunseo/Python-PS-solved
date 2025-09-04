import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
	m = int(input())
	lst.append(m)
for i in sorted(lst):
	print(i)