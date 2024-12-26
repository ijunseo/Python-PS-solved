num = int(input())
pivo = [0, 1, 1]
if num < 3:
    print(pivo[num])
else:
    for i in range(2, num):
        a = pivo[i - 1]
        b = pivo[i]
        pivo.append(a + b)
    print(pivo[-1])