import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))
now = lst[0]
if now > 1:
	print(1)
	sys.exit()
	
for i in range(1, n):
	if lst[i] <= now + 1:
		now += lst[i]
	else:
		print(now + 1)
		sys.exit()
print(now + 1)