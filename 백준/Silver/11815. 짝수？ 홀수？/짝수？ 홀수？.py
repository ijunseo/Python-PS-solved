#templet
import sys 
input = sys.stdin.readline

#input
n = int(input())
lst = list(map(int, input().split()))


for i in range(n):
    if lst[i] == (int(lst[i] ** 0.5) ** 2):
        print(1, end = " ")
        continue
    print(0, end = " ")
