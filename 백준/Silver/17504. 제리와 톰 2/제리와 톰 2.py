n = int(input())
lst = list(map(int, input().split()))
lst.reverse()
a, b = 1, 1

for i in range(len(lst)):
    if i == 0:
        b = lst[i]
        continue
    a = lst[i] * b + a
    a, b = b, a
print(b - a, b)