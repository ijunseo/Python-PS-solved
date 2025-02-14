import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
	lst = sorted(input().rstrip())
	if lst in st:
		continue
	else:
		st.append(lst)
print(len(st))