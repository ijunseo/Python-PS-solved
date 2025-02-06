#input 
num = int(input())
ans = 0

#solve
for i in range(1, 1_000_001):
	ans += (num // i) * i
#output
print(ans)