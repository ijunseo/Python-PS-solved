import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    name = input().rstrip()
    lst.append(name)

if lst == sorted(lst):
    print("INCREASING")
elif lst == sorted(lst, reverse= True):
    print("DECREASING")
else:
    print("NEITHER")