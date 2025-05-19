import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst1 = set(map(int, input().split()))
lst2 = set(map(int, input().split()))
ans = 0
ans += len(lst1 - lst2)
ans += len(lst2 - lst1)
print(ans)