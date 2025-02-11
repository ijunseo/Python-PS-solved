
#基本操作
import sys
input =sys.stdin.readline

#input 
n = int(input())
lst = sorted(set(list(map(int, input().split()))))
print(*lst)