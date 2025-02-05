import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
piv = 1
v = lst[0]
while piv < n:
	if v <= lst[piv]:
		v = lst[piv]
	else:
		if v % lst[piv]:
			num = (v // lst[piv]) + 1
			v = lst[piv] * num 
	piv += 1
print(v)