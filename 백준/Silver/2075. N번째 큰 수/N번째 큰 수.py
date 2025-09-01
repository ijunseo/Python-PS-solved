import sys
input = sys.stdin.readline
import heapq

n = int(input())
lst = []

for i in range(n):
    if i == 0:
        for n in map(int, input().split()):
            heapq.heappush(lst, n)
    else:
        for n in map(int, input().split()):
            if n > lst[0]:
                heapq.heappop(lst)
                heapq.heappush(lst, n)

print(lst[0])