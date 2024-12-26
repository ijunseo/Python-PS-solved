import sys
a, b = map(int, sys.stdin.readline().split())
passdict = {}
for i in range(a):
  c, d = sys.stdin.readline().split()
  passdict[c] = d
for i in range(b):
  e = sys.stdin.readline().strip()
  if e in passdict:
    print(passdict[e])