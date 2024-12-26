import sys
num = int(sys.stdin.readline())
lista = list(map(int, sys.stdin.readline().split()))
lista.sort(reverse = True)
listb = list(map(int, sys.stdin.readline().split()))
listb.sort()
ans = list(zip(lista, listb))
ansnum = 0
for i in ans:
    ansnum += i[0] * i[1]
print(ansnum)