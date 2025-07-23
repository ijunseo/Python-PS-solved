import sys
input = sys.stdin.readline
from collections import defaultdict
d = defaultdict(int)

n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
	d[lst[i]] += 1
	
m = int(input())
llst = list(map(int, input().split()))

for i in range(m):
	print(d[llst[i]], end = ' ')