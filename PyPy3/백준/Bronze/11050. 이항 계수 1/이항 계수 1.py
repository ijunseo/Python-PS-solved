import math
a , b = map(int, input().split())
c = 1
if b == 0:
  print("1")
else:
  for i in range(b):
    c *= a - i
  print(int(c/math.factorial(b)))