from collections import deque
#input
a,b = map(int, input().split())

#solve
went = [0] * 100001
q = deque([a])

while q:
    now = q.popleft()
    nowcst = went[now]
    if now == b:
        print(nowcst)
        exit()
    for i in [now + 1, now - 1, now * 2]:
        if 0 <= i <= 100000 and not went[i]:
            went[i] = nowcst + 1
            q.append(i)