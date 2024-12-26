import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
lielist = deque(list(map(int, input().split())))
lielist.popleft()
lieset = set(lielist)
peoplelist = []
for i in range(m):
    ex = deque(list(map(int, input().split())))
    ex.popleft()
    peoplelist.append(ex)
for i in range(m):
    for j in peoplelist:
        for k in j:
            if k in lieset:
                for l in j:
                    lieset.add(l)
    
ans = 0
def istrue(a):
    for i in a:
        if i not in lieset:
            continue
        else:
            return False
    return True
for i in peoplelist:
    if istrue(i) == True:
        ans += 1
    else:
        continue
print(ans)