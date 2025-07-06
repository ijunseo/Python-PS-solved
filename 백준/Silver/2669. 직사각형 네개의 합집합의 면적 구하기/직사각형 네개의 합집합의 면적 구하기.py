import sys
input = sys.stdin.readline

s = set()
while True:
    try:
        a, b, c, d = map(int, input().split())
        for i in range(a, c):
            for j in range(b, d):
                s.add((i, j))

    except:
        print(len(s))
        sys.exit()