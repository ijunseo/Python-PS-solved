from itertools import permutations
import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
lst = []

for i in range(n):
    num = input().strip()
    lst.append(num)
    
print(len(set("".join(i) for i in permutations(lst, k))))