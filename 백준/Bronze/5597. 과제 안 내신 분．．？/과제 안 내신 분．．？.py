import sys
input =sys.stdin.readline

lst = []
for _ in range(28):
    n = int(input())
    lst.append(n)
lst.sort()

piv = 1
for _ in range(28):
    now = lst.pop(0)
    if now == piv:
        piv += 1
    else:
        print(piv)
        piv += 2
if piv == 30:
    print('30')
