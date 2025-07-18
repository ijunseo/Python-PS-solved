import sys
input = sys.stdin.readline

n = int(input())
def find(n, st, mid, ed):
    if n == 1:
        print(st, ed)

    else:
        find(n - 1, st, ed, mid)
        print(st, ed)	
        find(n - 1, mid, st, ed)

print(2 ** n - 1)

find(n, 1, 2, 3)