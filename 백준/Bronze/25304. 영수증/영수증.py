ans = int(input())
n = int(input())
for _ in range(n):
    now, num = map(int, input().split())
    ans -= now * num
if not ans:
    print('Yes')
else:
    print('No')