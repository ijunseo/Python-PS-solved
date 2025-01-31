#基本操作
import sys
import heapq
input = sys.stdin.readline

#imput 
n, m, k = map(int, input().split())
line = [[] for _ in range(n + 1)]
is_connect = [False] * (n + 1)
k_list = list(map(int, input().split()))
q = []
cnt = 0
ans = 0
		
for _ in range(m):
	a, b, c = map(int, input().split())
	line[a].append((b, c))
	line[b].append((a, c))
	
for i in k_list:
	is_connect[i] = True
	cnt += 1
	for j in line[i]:
		heapq.heappush(q, (j[1], j[0]))
	
while q:
	cost, now = heapq.heappop(q)
	if is_connect[now]:
		continue
	is_connect[now] = True
	ans += cost
	cnt += 1 
	if cnt == n:
		print(ans)
		sys.exit()
	for i in line[now]:
		if is_connect[i[0]]:
			continue
		heapq.heappush(q, (i[1], i[0]))
		