import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if b >= 2 * a:
        if b % a:
            print(0)
        else:
            print(1)
    else:
        print(0)