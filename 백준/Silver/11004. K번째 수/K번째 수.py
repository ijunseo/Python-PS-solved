import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
print(lst[m - 1])
