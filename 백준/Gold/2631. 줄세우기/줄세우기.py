import sys
input = sys.stdin.readline
num = int(input())
numlist = [0]
for _ in range(num):
    numlist.append(int(input()))
dplist = [0] * (num + 1)
for i in range(1, num + 1):
    piv = i - 1
    while piv >= 0:
        if numlist[i] > numlist[piv]:
            dplist[i] = max(dplist[i], dplist[piv] + 1)
        piv -= 1
print(num - max(dplist))