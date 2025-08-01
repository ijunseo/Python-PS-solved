import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(9)]

mx = 0
for i in range(9):
	mx = max(max(lst[i]), mx)

print(mx)
for i in range(9):
	for j in range(9):
		if lst[i][j] == mx:
			print(i + 1, j + 1)
			sys.exit()