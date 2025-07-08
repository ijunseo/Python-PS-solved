import sys
input = sys.stdin.readline

n = int(input())

enter = set()
leave = set()

for _ in range(n):
    a, b = map(str, input().split())
    if b == 'enter':
        enter.add(a)
    else:
        enter.remove(a)
for i in sorted(enter, reverse= True):
    print(i)