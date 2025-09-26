import sys
import heapq
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
	n = int(input())
	lst = list(map(int, input().split()))
	lst.sort()
	ans = 0
	for _ in range(n - 1):
		a = heapq.heappop(lst)
		b = heapq.heappop(lst)
		ans += a + b
		heapq.heappush(lst, a + b)
	print(ans)
	