import sys
import copy
a, b = map(int, sys.stdin.readline().split())
numlist = []
for i in range(a):
    imsi = list(map(int,sys.stdin.readline().split()))
    numlist.append(imsi)
kijun = [[0] * a for i in range(a)]
for i in range(a):
    kijun[i][i] = 1
marlist = {}

# def kake(mar):
#     imsilist = copy.deepcopy(mar)
#     returnlist = [[0] * a for i in range(a)]
#     for i in range(a):
#         for j in range(a):
#             ans = 0
#             for k in range(a):
#                 ans += imsilist[i][k] * imsilist[k][j]
#             returnlist[i][j] = ans % 1000
#     return(returnlist)

def kake1(mar1, mar2):
    returnlist = [[0] * a for i in range(a)]
    for i in range(a):
        for j in range(a):
            ans = 0
            for k in range(a):
                ans += mar1[i][k] * mar2[k][j]
            
            returnlist[i][j] = ans % 1000
    return(returnlist)


def find(a):
    if a == 1:
        return(kake1(numlist, kijun))

            
    if a in marlist:
        return(marlist[a])

    if a % 2 == 1:
        result = kake1(find(a - 1), numlist)
    
    else:
        half = find(a//2)
        result = kake1(half, half)
    
    marlist[a] = result
    return result #もっと工夫する必要ありそう。

ans = find(b)
for i in ans:
    print(*i)