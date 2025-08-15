import sys
input = sys.stdin.readline

s = set()


n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    if a == 'ChongChong' or b == 'ChongChong':
        s.add(a)
        s.add(b)
        continue 

    if a in s:
        s.add(b)
    elif b in s:
        s.add(a)
print(len(s))


