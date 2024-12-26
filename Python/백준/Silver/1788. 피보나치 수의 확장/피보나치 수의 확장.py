num = int(input())

if num < 0:
    num1 = -num
else:
    num1 = num

pivolist = [0,1]
for i in range (num1 - 1):
    pivolist.append((pivolist[-1] + pivolist[-2]) % 1000000000)
if num < 0 and num1 % 2 == 0:
    print('-1')
    print(pivolist[num1])
elif num == 0:
    print('0')
    print('0')
else:
    print('1')
    print(pivolist[num1])