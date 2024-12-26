import sys
input = sys.stdin.readline
num = int(input())
num_1 = str(num)
def length(a):
    a = list(a)
    a = int(len(a))
    return a
ans = 0
for i in range (1, length(num_1)):
    ans += 9 * 10 ** (i - 1) * i
ans +=(num - 10 ** (length(num_1) - 1) + 1) * length(num_1)
print(ans)