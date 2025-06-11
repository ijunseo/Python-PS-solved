lst = []
for _ in range(8):
    n = int(input())
    lst.append(n)
    
llst = sorted(lst)
print(sum(llst[3:]))

lllst = []
for i in range(5):
    now = llst[- i - 1]
    for j in range(8):
        if lst[j] == now:
        	lllst.append(j + 1)
print(*sorted(lllst))
    