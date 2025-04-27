import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    lst = list(map(int, input().split()))
    llst = [0] * (n)
    ans = 0
    for i in range(n):
        if not llst[i]:
            ans += 1
            piv = i
            while True:
                next_piv = lst[piv] - 1
                if not llst[next_piv]:
                    llst[next_piv] = 1
                    piv = next_piv
                else:
                    break
    print(ans)
