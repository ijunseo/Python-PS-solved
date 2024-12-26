num = list(map(str, input()))
for i in num:
    i = int(i)
num.sort(reverse=True)
for i in num:
    print(i, end = '')