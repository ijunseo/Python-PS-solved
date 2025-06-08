import sys
from collections import deque
input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.q = deque([])
    
    def push(self, num):
        self.q.append(num)

    def pop(self):
        try:
            return self.q.popleft()
        except:
            return -1

    def size(self):
        return len(self.q)
    
    def empty(self):
        if self.q:
            return 0
        else:
            return 1
        
    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1
        
    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1
        
n = int(input())
q = Deque()

for _ in range(n):
    cmd = list(map(str, input().split()))
    if len(cmd) == 2:
        q.q.append(int(cmd[1]))
    else:
        print(getattr(q, cmd[0])())