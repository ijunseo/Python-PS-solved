import sys
import itertools
a, b = map(int, sys.stdin.readline().split())
numlist = sorted(map(int, sys.stdin.readline().split()))
anslist = itertools.combinations_with_replacement(numlist, b)
for i in anslist:
  print(*i)