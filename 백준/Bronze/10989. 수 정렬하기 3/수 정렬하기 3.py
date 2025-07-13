from collections import defaultdict
import sys
input = sys.stdin.readline

d = defaultdict(int)
n = int(input())
for _ in range(n):
    a = int(input())
    d[a] += 1
for i in sorted(d):
    for _ in range(d[i]):
        print(i)