import sys
num = int(sys.stdin.readline())
for i in range(num):
  a, b, c = map(int, sys.stdin.readline().split())
  d = a % 2 + b % 2 + c % 2
  if d % 2 == 1:
    print('NO')
  else:
    print('YES')