tc = int(input())

for _ in range(tc):
    a, b, a1, b1 = map(int, input().split())
    ans = 0
    bans = b * b1
    aans = a * a1
    ans = max(aans, bans)
    while True:
        newans = max(aans - a, bans + a)
        if ans > newans:
            aans -= a
            bans += a
            ans = newans
        else:
            break
    print(ans)