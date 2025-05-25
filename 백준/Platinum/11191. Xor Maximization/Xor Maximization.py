import sys
input = sys.stdin.readline 

n = int(input())
basis = []
lst = list(map(int, input().split()))

for i in lst:
    for j in basis:
        i = min(i, i ^ j)

    if i:
        basis.append(i)

mx = 0
for i in sorted(basis, reverse= True):
    mx = max(mx, mx ^ i)
print(mx)