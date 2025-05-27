import sys
input = sys.stdin.readline

n = str(input().rstrip())

tar = n[0]
piv = 1
lst = []

for i in range(len(n) - 1):
    if n[piv] != tar:

        lst.append(tar)
        if tar == '0':
            tar = '1'
        else:
            tar = '0'
    piv += 1
lst.append(n[-1])
a = lst.count('0')
b = lst.count('1')
print(min(a, b))