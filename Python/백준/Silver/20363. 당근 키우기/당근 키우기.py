#input
a, b = map(int, input().split())

if a<= b:
	print(b + a + a//10)
else:
	print(a + b + b//10)