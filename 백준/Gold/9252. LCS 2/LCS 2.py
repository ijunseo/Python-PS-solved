import sys
lista = [0] + list(map(str, sys.stdin.readline().rstrip()))
listb = [0] + list(map(str, sys.stdin.readline()))
lena = len(lista)
lenb = len(listb)
dplist = [['' for _ in range(lena)] for _ in range(lenb)]


for i in range(1, lenb):
    for j in range(1, lena):
        if lista[j] == listb[i]:
            dplist[i][j] = dplist[i - 1][j - 1] + str(lista[j])
        else:
        	if len(dplist[i][j - 1]) > len(dplist[i - 1][j]):
        		dplist[i][j] = dplist[i][j - 1]
        	else:
        		dplist[i][j] = dplist[i - 1][j]
ans = dplist[-1][-1]
if len(ans) != 0:
	print(len(ans))
	print(ans)
else:
	print('0')