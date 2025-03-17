import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
	st = input().rstrip()
	print(st[0], end = '')
	print(st[-1])