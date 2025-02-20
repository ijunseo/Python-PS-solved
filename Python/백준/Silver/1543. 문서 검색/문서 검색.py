import sys
input = sys.stdin.readline

#input
n = input().rstrip()
m = input().rstrip()

#solve
piv = 0
ans = 0
while piv < len(n):
	i = 0
	while i != len(m) and piv + i < len(n):
		if n[piv + i] == m[i]:
			i += 1 
			if i == len(m):
				ans += 1 
				piv = piv + i - 1
				break
		else:
			break
	piv += 1
#ans
print(ans)