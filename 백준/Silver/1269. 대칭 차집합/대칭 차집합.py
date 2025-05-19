import sys
input = sys.stdin.readline
'''
差集合を計算する
Pythonのsetｆでは
-で差集合の計算ができるので
計算に用いた
'''
n, m = map(int, input().split())

lst1 = set(map(int, input().split()))
lst2 = set(map(int, input().split()))
ans = 0
ans += len(lst1 - lst2)
ans += len(lst2 - lst1)
print(ans)