import sys
input = sys.stdin.readline

while True:
    cmd = input().rstrip()
    if not cmd:
        break
    ans = 0
    a, b = map(int, cmd.split())
    for i in range(a, b + 1):
        if len(set(str(i))) == len(str(i)):
            ans += 1
    print(ans)