import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

lst.sort(reverse=True)
print(lst[0] + lst[1])
