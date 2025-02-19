#基本操作
import sys
input = sys.stdin.readline

#input 
n, m = map(int, input().split())
a = n // 2
b = n ** 2 - a ** 2
c = b + a ** 2

#output
print(c * m)