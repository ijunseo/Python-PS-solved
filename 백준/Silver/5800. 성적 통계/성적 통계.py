import sys
input = sys.stdin.readline
num = int(input())
for i in range(num):
    anslist = list(map(int, input().split()))
    anslist = anslist[1:]
    anslist.sort()

    print("Class", i + 1)
    print("Max", anslist[-1], end =', ')
    print("Min", anslist[0], end =', ')
    print('Largest gap', max(anslist[i + 1] - anslist[i] for i in range(len(anslist) - 1)))