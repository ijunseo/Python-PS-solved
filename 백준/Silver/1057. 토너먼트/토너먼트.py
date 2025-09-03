a, b, c = map(int , input().split())

ans = 0
while b != c:
	b -= b // 2
	c -= c // 2
	ans += 1
	
print(ans)