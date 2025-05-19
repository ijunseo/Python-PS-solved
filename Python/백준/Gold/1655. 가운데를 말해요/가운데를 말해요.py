import sys
input = sys.stdin.readline
write = sys.stdout.write
import heapq

n = int(input())
min_q = []
max_q = []
ans_lst = []
ans = int(input())
ans_lst.append(str(ans))

for i in range(n - 1):
	now = int(input())
	#print('now', now)
	if now > ans:
		if len(min_q) < len(max_q):
			heapq.heappush(min_q, -ans)
			heapq.heappush(max_q, now)
			ans = heapq.heappop(max_q)
		else:
			heapq.heappush(max_q, now)
		ans_lst.append(str(ans))

	else:
		if len(min_q) < len(max_q):
			heapq.heappush(min_q, -now)
		else:
			heapq.heappush(max_q, ans)
			heapq.heappush(min_q, -now)
			ans = - heapq.heappop(min_q)
		ans_lst.append(str(ans))
	
	#print(ans, min_q, max_q)

for i in ans_lst:
	write(i + '\n')