lst = list(map(int, input().split()))
one = 0
two = 0

for i in range(len(lst)):
    if lst[i] == 1:
        one += 1
    else:
        two += 1

if one > two:
    print(1)
else:
    print(2)