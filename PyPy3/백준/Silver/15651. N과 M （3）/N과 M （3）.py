import itertools
num1, num2 = map(int,input().split())
num1list = []
for i in range(num1):
    num1list.append(i + 1)
list1 = list(itertools.product(num1list,repeat = num2))
for i in list1:
    print(*i)