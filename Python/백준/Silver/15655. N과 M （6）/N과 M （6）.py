import itertools
import sys
num1, num2 = map(int, sys.stdin.readline().split())
numlist = sorted(map(int, sys.stdin.readline().split()))
ans = itertools.combinations(numlist, num2)
for i in ans:
    print(*i)