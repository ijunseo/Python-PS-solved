import sys 
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append([a, b])
        if a == 1:
            mx = b
    lst.sort()
    ans = 0

    for i in range(n):
        if lst[i][1] <= mx:
            mx = lst[i][1]
            ans += 1

    print(ans)
    