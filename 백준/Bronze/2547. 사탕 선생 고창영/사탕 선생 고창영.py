import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    _ = input() 
    n = int(input())
    ans = 0
    for _ in range(n):
        ans += int(input())
    if ans % n == 0:
        print("YES")
    else:
        print("NO")