import math
a, b = map(int, input().split())
c = math.comb(a + b - 1, b - 1)
print(c % 1000000000) 