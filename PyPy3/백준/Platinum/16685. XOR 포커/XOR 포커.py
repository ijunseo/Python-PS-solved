import sys
input = sys.stdin.readline

n = int(input())
basis = []
basnum = int(input())
for num_piv in range(n - 1):
	nownum = int(input())
	nownum ^= basnum
	for bas in basis:
		nownum = min(nownum, nownum ^ bas)
	if nownum:
		basis.append(nownum)

ans = 0
for check_num in sorted(basis, reverse = True):
	ans = max(ans, ans ^ check_num)
print(ans)