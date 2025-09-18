
n = int(input())
lst = []
for _ in range(n):
    lst.append(str(input()))
for i in range(1, len(lst[0]) + 1):
    ans = []
    for j in range(n):
        if lst[j][-i:] in ans:
            break
        else:
            ans.append(lst[j][-i:])
    if len(ans)==n:
        print(i)
        break