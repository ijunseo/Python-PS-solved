import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n = int(input())
for _ in range(n):  
    #print(q)
    cmd = list(map(str, input().split()))
    #print(cmd)
    if cmd[0] == 'push':
            q.append(int(cmd[1]))

    elif cmd[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print('-1')

    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print('-1')

    elif cmd[0] == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')

    elif cmd[0] == 'size':
        print(len(q))

    elif cmd[0] == 'empty':
        if q:
            print('0')
        else:
            print('1')