import sys 
import heapq
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort()

anslst = [0]
piv = 0

while piv < n:
    nowmin = heapq.heappop(anslst)
    nowst, nowed = lst[piv][0], lst[piv][1]

    if nowst >= nowmin:
        heapq.heappush(anslst, nowed)
    else:
        heapq.heappush(anslst, nowmin)
        heapq.heappush(anslst, nowed)
    piv += 1

print(len(anslst))