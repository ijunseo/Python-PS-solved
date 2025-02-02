#基本操作
import sys
input = sys.stdin.readline
from collections import deque


#input
n = int(input())
lst = deque(map(int, input().split()))
imsi = deque()
imsi.append(0)
lst.append(0)
target = 1

while target != n:
    if target == imsi[-1]:
        imsi.pop()
        target += 1
    elif target == lst[0]:
        lst.popleft()
        target += 1
    else:
        now = lst.popleft()
        if now == 0:
            print('Sad')
            sys.exit()
        imsi.append(now)
    
print('Nice')