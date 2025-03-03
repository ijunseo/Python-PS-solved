#基本操作
import sys
input = sys.stdin.readline
from collections import deque


#input
a, b = map(int, input().split())

#solve
lenlst = [0] * 100001
wentlst = [0] * 100001
#bfs
q = deque([(a,0)])
while q:
	now,cost = q.popleft()
	if cost > lenlst[now]:
		continue
	if now == b:
		print(cost)
		lst = []
		piv = b
		for i in range(cost + 1):
			lst.append(piv)
			piv = wentlst[piv]
		print(*lst[::-1])
		sys.exit()
	for i in [now * 2, now - 1, now + 1]:
		if i < 0 or i > 100000:
			continue
		if not lenlst[i]:
			lenlst[i] = cost + 1
			wentlst[i] = now
			q.append((i, cost + 1))
		else:
			if lenlst[i] > cost + 1:
				lenlst[i] = cost + 1
				wentlist[i] = now
				q.append((i, cost + 1))
