n = int(input())
for _ in range(n):
    now = len(input().rstrip())
    if 6 <= now <= 9:
        print('yes')
    else:
        print('no')