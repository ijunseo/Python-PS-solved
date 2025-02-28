from collections import deque

#input
a, b = map(int, input().split())

#solve
ans = 0
went = [0] * 100001
q = deque([a])

while q:
	now = q.popleft()
	if now == b:
		ans += 1
		continue
	
	for i in [now + 1, now - 1, now * 2]:
		if i >= 0 and i < 100001:
			if went[i] == went[now] + 1:
				q.append(i)
			if not went[i]:#訪問したことないなら
				went[i] = went[now] + 1
				q.append(i)

print(went[b])
print(ans)