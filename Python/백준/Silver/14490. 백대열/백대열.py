#基本操作
import sys
input = sys.stdin.readline
import math
#input
a,b = map(int, input().split(':'))
c = math.gcd(a, b)

#output
print(f'{a // c}:{b // c}')