import sys
input = sys.stdin.readline
n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(sum(map(abs, lst1)) + sum(map(abs, lst2)))
