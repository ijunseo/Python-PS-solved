a, b = map(int,input().split())

count = 1
while a != b:
    count += 1
    c = b
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    if c == b:
        print("-1")
        break
else:
    print(count)