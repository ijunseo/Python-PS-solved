import sys
import itertools
a, b = map(int, sys.stdin.readline().split())
numlist = sorted(set(map(int, sys.stdin.readline().split())))
anslist = itertools.combinations_with_replacement(numlist, b)#setで重複する要素を除去
for i in anslist:
  print(*i)