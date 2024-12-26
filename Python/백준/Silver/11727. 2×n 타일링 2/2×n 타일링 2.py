import sys
num = int(sys.stdin.readline())
dplist = [1, 1]
for i in range(num - 1):
    dplist.append((2 * dplist[i] + dplist[i + 1]))
print(dplist[-1] % 10007)